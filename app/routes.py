from flask import Blueprint, render_template, request, jsonify
from app.gemini_client import GeminiClient
from app.database import Database
import re

main = Blueprint('main', __name__)
gemini_client = GeminiClient()
db = Database()

# List of concerning symptoms that should trigger immediate emergency warning
EMERGENCY_SYMPTOMS = [
    'chest pain', 'difficulty breathing', 'shortness of breath', 'severe bleeding',
    'sudden weakness', 'slurred speech', 'severe headache', 'suicidal', 'homicidal',
    'unconscious', 'seizure', 'stroke', 'heart attack', 'choking', 'burning',
    'poison', 'overdose', 'anaphylaxis', 'broken bone', 'deep cut'
]

def contains_emergency_symptoms(symptoms):
    """Check if symptoms contain emergency indicators"""
    symptoms_lower = symptoms.lower()
    for emergency_symptom in EMERGENCY_SYMPTOMS:
        if emergency_symptom in symptoms_lower:
            return True
    return False

def validate_symptoms_input(symptoms):
    """Validate and sanitize symptoms input"""
    if not symptoms or len(symptoms.strip()) == 0:
        return False, "Please describe your symptoms"
    
    if len(symptoms.strip()) < 10:
        return False, "Please provide more detailed symptoms (at least 10 characters)"
    
    if len(symptoms) > 1000:
        return False, "Symptoms description too long. Please summarize to under 1000 characters."
    
    # Check for inappropriate content
    inappropriate_patterns = [
        r'\b(?:fuck|shit|asshole|bitch|dick|pussy|cunt)\b',
        r'\b(?:kill|murder|harm|hurt)\s+(?:myself|yourself|themselves|someone)\b'
    ]
    
    for pattern in inappropriate_patterns:
        if re.search(pattern, symptoms, re.IGNORECASE):
            return False, "Please provide appropriate medical symptoms only"
    
    return True, "Valid"

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/check_symptoms', methods=['POST'])
def check_symptoms():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', '').strip()
        
        # Validate input
        is_valid, message = validate_symptoms_input(symptoms)
        if not is_valid:
            return jsonify({'error': message}), 400
        
        # Check for emergency symptoms
        emergency_warning = ""
        if contains_emergency_symptoms(symptoms):
            emergency_warning = "🚨 URGENT: Your symptoms may indicate a medical emergency. Please seek immediate medical attention or call emergency services!"
        
        # Analyze symptoms using Gemini
        analysis = gemini_client.analyze_symptoms(symptoms)
        
        # Add emergency warning if needed
        if emergency_warning:
            analysis = emergency_warning + "\n\n" + analysis
        
        # Save to database
        db.save_query(symptoms, analysis)
        
        return jsonify({
            'analysis': analysis,
            'symptoms': symptoms,
            'has_emergency_warning': bool(emergency_warning)
        })
        
    except Exception as e:
        logging.error(f"Symptom analysis error: {e}")
        return jsonify({'error': 'An error occurred while analyzing symptoms. Please try again.'}), 500

@main.route('/history')
def get_history():
    try:
        history = db.get_history(limit=10)
        history_list = [
            {
                'symptoms': item[0],
                'response': item[1],
                'timestamp': item[2]
            }
            for item in history
        ]
        return jsonify(history_list)
    except Exception as e:
        logging.error(f"History fetch error: {e}")
        return jsonify({'error': 'Unable to fetch history'}), 500

@main.route('/emergency_info')
def emergency_info():
    """Provide emergency contact information"""
    emergency_data = {
        "emergency_contacts": {
            "india": {
                "emergency": "112 or 108",
                "police": "100", 
                "fire": "101",
                "ambulance": "102"
            },
            "general": {
                "emergency": "Local emergency services",
                "advice": "Call immediately for: Chest pain, Difficulty breathing, Severe bleeding, Stroke symptoms"
            }
        }
    }
    return jsonify(emergency_data)