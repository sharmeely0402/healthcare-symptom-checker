# 🏥 Healthcare Symptom Checker - Educational Tool

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-AI-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**An AI-powered educational tool for symptom analysis using Google's Gemini AI**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-reference) • [Safety](#-safety-features)

</div>

## ⚠️ Critical Medical Disclaimer

> **🚨 IMPORTANT: This is an EDUCATIONAL TOOL only - NOT for medical diagnosis!**
> 
> - **NOT a substitute for professional medical advice**
> - **ALWAYS consult healthcare professionals for medical concerns**
> - **NEVER use for emergency situations**
> - **DO NOT self-diagnose or self-medicate based on this tool**
> - **In emergencies, call emergency services immediately**

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Safety Features](#-safety-features)
- [Technical Architecture](#-technical-architecture)
- Testing & Accuracy](#-testing--accuracy)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Overview

The **Healthcare Symptom Checker** is an educational web application that uses Google's Gemini AI to provide information about possible health conditions based on described symptoms. It's designed as a learning tool to help users understand potential health conditions while emphasizing the importance of professional medical consultation.

### Key Principles:
- 🔬 **Educational Focus**: Learn about health conditions and symptoms
- 🛡️ **Safety First**: Multiple layers of medical disclaimers
- 🤖 **AI-Powered**: Leverages Google's Gemini AI for analysis
- 💾 **History Tracking**: Maintains query history for reference
- 📱 **Web Accessible**: Responsive design for all devices

## ✨ Features

### Core Functionality
- **🤒 Symptom Analysis**: AI-powered analysis of described symptoms
- **📚 Educational Content**: Information about possible conditions
- **🔄 Query History**: Persistent storage of previous analyses
- **📊 Accuracy Dashboard**: Test and evaluate AI performance
- **📈 Visualization**: Charts and metrics for performance analysis

### User Experience
- **🎨 Modern UI**: Clean, responsive Bootstrap interface
- **⚡ Real-time Processing**: Instant AI analysis
- **📱 Mobile-Friendly**: Works on all device sizes
- **🔍 History Search**: Easy access to previous queries
- **📋 Structured Results**: Consistent, easy-to-read format

### Safety & Compliance
- **⚠️ Prominent Disclaimers**: Multiple safety warnings
- **🎓 Educational Emphasis**: Clear purpose statements
- **🚑 Emergency Guidance**: Instructions for urgent situations
- **👨‍⚕️ Professional Referral**: Always recommends consulting doctors

## 🎥 Demo

### Live Demo
Access the application: `http://localhost:5000` (after installation)

### Demo Video
[Watch the demonstration video](#) *(Link to be added)*

### Sample Interaction
**Input Symptoms:**
```
Headache, fever, and fatigue for 2 days with occasional chills
```

**AI Response:**
```
POSSIBLE CONDITIONS:
- Viral Infection: Common symptoms include headache, fever, and fatigue
- Influenza: Seasonal flu often presents with these symptoms
- Common Cold: Mild viral infection with headache and fatigue

RECOMMENDED NEXT STEPS:
- Rest and adequate hydration
- Monitor temperature regularly
- Consult healthcare provider if symptoms worsen
- Consider over-the-counter fever reducers if appropriate

IMPORTANT DISCLAIMERS:
- This is for educational purposes only and not a substitute for professional medical advice
- Always consult with a healthcare professional for proper diagnosis
- In case of emergency, seek immediate medical attention
- Do not self-diagnose or self-medicate based on this information
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- Git (optional)

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/healthcare-symptom-checker.git
   cd healthcare-symptom-checker
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```bash
   # Create .env file
   echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
   echo "SECRET_KEY=your-secret-key-here" >> .env
   ```

5. **Get Gemini API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Replace `your_actual_api_key_here` in `.env` with your key

6. **Initialize Database**
   ```bash
   python init_db.py
   ```

7. **Run the Application**
   ```bash
   python run.py
   ```

8. **Access the Application**
   Open your browser and navigate to: `http://localhost:5000`

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
# Required: Google Gemini API Key
GEMINI_API_KEY=your_actual_gemini_api_key_here

# Required: Flask secret key for session security
SECRET_KEY=your-secret-key-here

# Optional: Database configuration
DATABASE_PATH=healthcare.db

# Optional: Application settings
DEBUG=False
PORT=5000
HOST=0.0.0.0
```

### Database Configuration
The application uses SQLite by default. The database file (`healthcare.db`) is automatically created in the project root.

## 💻 Usage

### Basic Symptom Checking
1. **Access the Web Interface**
   - Open `http://localhost:5000` in your browser

2. **Describe Symptoms**
   - Enter detailed symptom descriptions in the text area
   - Example: "headache for 2 days, fever of 101°F, fatigue"

3. **Analyze Symptoms**
   - Click "Analyze Symptoms" button
   - Wait for AI processing (typically 2-5 seconds)

4. **Review Results**
   - Read the educational analysis
   - Note the important disclaimers
   - Follow recommended next steps

### Advanced Features

#### Query History
- Access previous analyses from the "Recent Analyses" section
- View details of past queries
- Use for educational reference

#### Accuracy Dashboard
- Access via `/accuracy_dashboard`
- Test AI performance with predefined cases
- View accuracy metrics and charts

## 🔌 API Reference

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. Analyze Symptoms
```http
POST /check_symptoms
Content-Type: application/json

{
  "symptoms": "headache, fever, fatigue"
}
```

**Response:**
```json
{
  "analysis": "POSSIBLE CONDITIONS:\n- Condition 1...",
  "symptoms": "headache, fever, fatigue"
}
```

#### 2. Get Query History
```http
GET /history
```

**Response:**
```json
[
  {
    "symptoms": "headache, fever",
    "response": "POSSIBLE CONDITIONS:\n- ...",
    "timestamp": "2024-01-15 10:30:00"
  }
]
```

#### 3. Accuracy Dashboard
```http
GET /accuracy_dashboard
```

#### 4. Run Accuracy Tests
```http
POST /run_accuracy_test
Content-Type: application/json

{
  "test_case_ids": [1, 2, 3]
}
```

## 🛡️ Safety Features

### Multiple Safety Layers

1. **Frontend Disclaimers**
   - Prominent warning banners on every page
   - Clear educational purpose statements
   - Emergency contact information

2. **AI Prompt Engineering**
   ```python
   "ACT AS A MEDICAL EDUCATIONAL TOOL ONLY. Provide educational information without making definitive diagnoses."
   ```

3. **Response Formatting**
   - Structured output prevents ambiguous responses
   - Mandatory disclaimer sections
   - No specific treatment recommendations

4. **Input Validation**
   - Minimum symptom description length
   - Content filtering for inappropriate requests
   - Rate limiting protection

### Compliance Features
- **No Personal Data Storage**: Minimal data retention
- **Educational Purpose**: Clear intent documentation
- **Professional Guidance**: Always recommends doctor consultation
- **Emergency Protocols**: Clear instructions for urgent situations

## 🏗️ Technical Architecture

### System Overview
```
Frontend (HTML/CSS/JS) 
    ↓
Flask Web Server (Python)
    ↓
Gemini AI API (Google)
    ↓
SQLite Database
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Flask (Python) | Web server & API |
| **AI Engine** | Google Gemini API | Symptom analysis |
| **Database** | SQLite | Query history storage |
| **Frontend** | Bootstrap 5 + JavaScript | User interface |
| **Charts** | Chart.js | Accuracy visualization |

### Project Structure
```
healthcare-symptom-checker/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # API routes & handlers
│   ├── gemini_client.py     # Gemini AI integration
│   └── database.py          # Database operations
├── tests/                   # Test suites
├── templates/               # HTML templates
├── static/                  # CSS, JS, assets
├── requirements.txt         # Python dependencies
├── run.py                  # Application entry point
└── healthcare.db           # SQLite database (auto-created)
```

## 📈 Testing & Accuracy

### Accuracy Evaluation
The application includes comprehensive testing features:

1. **Predefined Test Cases**
   - Common symptom patterns
   - Various severity levels
   - Expected condition mappings

2. **Performance Metrics**
   - Precision and recall calculations
   - Condition matching accuracy
   - Response quality scoring

3. **Visual Analytics**
   - Accuracy trend charts
   - Condition detection rates
   - Performance comparison graphs

### Running Tests
```bash
# Unit tests
python -m pytest tests/

# Accuracy evaluation
python tests/accuracy_evaluation.py

# Load testing
python tests/load_test.py
```

## 🔧 Troubleshooting

### Common Issues

1. **API Key Errors**
   ```
   Error: GEMINI_API_KEY not found
   ```
   **Solution**: Verify `.env` file exists and contains valid API key

2. **Module Not Found**
   ```
   ModuleNotFoundError: No module named 'google'
   ```
   **Solution**: Run `pip install -r requirements.txt`

3. **Port Already in Use**
   ```
   Address already in use
   ```
   **Solution**: Change port in `run.py` or kill existing process

4. **Database Errors**
   ```
   SQLite OperationalError
   ```
   **Solution**: Delete `healthcare.db` and restart application

### Debug Mode
Enable debug mode for detailed error logging:
```python
# In run.py
app.run(debug=True, host='0.0.0.0', port=5000)
```

## 🤝 Contributing

We welcome contributions! Please read our contributing guidelines:

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

### Code Standards
- Follow PEP 8 Python style guide
- Include docstrings for all functions
- Add tests for new features
- Update documentation accordingly

### Areas for Contribution
- Additional test cases
- UI/UX improvements
- Accuracy metrics enhancement
- Multi-language support
- Additional safety features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses
- Flask: BSD License
- Bootstrap: MIT License
- Google Gemini AI: Google Terms of Service

## 🙏 Acknowledgments

- **Google Gemini AI** for providing the AI capabilities
- **Flask Community** for the excellent web framework
- **Medical Professionals** who reviewed the safety features
- **Open Source Community** for various libraries and tools

## 📞 Support

For technical support or questions:
- 📧 Email: support@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/healthcare-symptom-checker/issues)
- 📚 Documentation: [Project Wiki](https://github.com/yourusername/healthcare-symptom-checker/wiki)

---

<div align="center">

**⚠️ REMEMBER: This tool is for EDUCATIONAL PURPOSES ONLY. Always consult healthcare professionals for medical advice.**

Made with ❤️ for better health education

</div>
