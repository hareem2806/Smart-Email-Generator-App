# 📧 Smart AI Email Generator (Flask + Streamlit + Ollama)

A smart AI-powered email generator that creates professional, context-aware emails.  
Users can input recipient type, subject, date, background, tone, and style — the system dynamically generates a polished email.

## 🚀 Live Demo
👉 Try it here: [https://random-ngrok-link.ngrok-free.app]( https://2366594aec7c.ngrok-free.app)  

*(Note: The link works only while my local server is running.)*

## 🚀 Features
- Flask backend using **Ollama (Llama 3.2:latest)** for text generation  
- Streamlit frontend for an interactive UI  
- Dropdowns & text fields for recipient, salutation, and email context  
- Generates ready-to-copy professional emails  


## 🛠️ Tech Stack
- **Python**
- **Flask** (backend API)
- **Streamlit** (frontend UI)
- **Ollama (Llama 3.2 model)**

## Setup
git clone https://github.com/yourusername/email-generator.git
cd email-generator
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
ollama pull llama3.2:latest
python app.py
streamlit run streamlit_app.py



