import sqlite3
import datetime
import logging

class Database:
    def __init__(self, db_path='healthcare.db'):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS query_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symptoms TEXT NOT NULL,
                    response TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Create index for better performance
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_timestamp 
                ON query_history(timestamp DESC)
            ''')
            
            conn.commit()
            conn.close()
            logging.info("Database initialized successfully")
            
        except sqlite3.Error as e:
            logging.error(f"Database initialization error: {e}")
    
    def save_query(self, symptoms, response):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO query_history (symptoms, response, timestamp)
                VALUES (?, ?, ?)
            ''', (symptoms, response, datetime.datetime.now()))
            
            conn.commit()
            conn.close()
            
        except sqlite3.Error as e:
            logging.error(f"Database save error: {e}")
    
    def get_history(self, limit=10):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT symptoms, response, timestamp 
                FROM query_history 
                ORDER BY timestamp DESC 
                LIMIT ?
            ''', (limit,))
            
            history = cursor.fetchall()
            conn.close()
            
            return history
            
        except sqlite3.Error as e:
            logging.error(f"Database fetch error: {e}")
            return []