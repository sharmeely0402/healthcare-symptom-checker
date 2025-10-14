from flask import Flask
import os
import logging
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s %(message)s',
        handlers=[
            logging.FileHandler('healthcare_app.log'),
            logging.StreamHandler()
        ]
    )
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app