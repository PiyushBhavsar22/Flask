# **FLASK FUSION**

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)  
[![Framework](https://img.shields.io/badge/framework-Flask-red)](https://flask.palletsprojects.com/)

## **Overview**

Flask Fusion is a web application built using Flask, a lightweight Python web framework. The application demonstrates API Integration, offering Performance. It is designed to be Basic API Intergration Project.
## **Features**

- 🔹 **[Feature 1]**: Allows embedding Python code into HTML, rendering dynamic content.
- 🔹 **[Feature 2]**: Allows users to test APIs with different request types (GET, POST, PUT, DELETE, etc.).
- 🔹 **[Feature 3]**: Displays responses in JSON format.

## **Technology Stack**

- **Backend**: Flask (Python)  
- **Frontend**: HTML  
- **API Testing**: Postman 
- **Others**: Jinja2

## **Getting Started**

Follow these steps to set up the project locally:

### **Prerequisites**
Ensure you have the following installed on your machine:
- Python 3.x
- pip (Python package installer)

### **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/PiyushBhavsar22/Flask.git
   cd Flask
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (if required):
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development  # For debugging
   ```

5. Run the application:
   ```bash
   flask run
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

### **Directory Structure**
```
Flask/
│
├── app/                # Main application code
│   ├── static/         # Static files (CSS, JS, images)
│   ├── templates/      # HTML templates
│   ├── routes.py       # Application routes
│   ├── models.py       # Database models (if applicable)
│   └── __init__.py     # Flask app initialization
│
├── tests/              # Test cases
│
├── requirements.txt    # Python dependencies
├── config.py           # Configuration settings
├── README.md           # Project documentation
└── app.py              # Main application entry point
```
 
