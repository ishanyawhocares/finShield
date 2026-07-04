from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load the trained model
# We check if the file exists to prevent crashing if you forgot to run train_model.py
MODEL_PATH = 'phishing_model.pkl'
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("✅ AI Model Loaded Successfully")
else:
    model = None
    print("⚠️ Warning: Model not found. Please run train_model.py first.")

def extract_features(url):
    """
    MUST match the exact same logic used in train_model.py
    """
    features = []
    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(url.count('@'))
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    features.append(1 if re.search(ip_pattern, url) else 0)
    features.append(1 if "https" in url else 0)
    
    # Convert to numpy array and reshape for single prediction
    return np.array(features).reshape(1, -1)

@app.route('/scan', methods=['POST'])
def scan_url():
    data = request.json
    url = data.get('url', '')
    
    if not model:
        return jsonify({"status": "ERROR", "message": "AI Model not loaded", "color": "gray"})

    # 1. Extract features from the new URL
    features = extract_features(url)
    
    # 2. Ask the model to predict (0 = Safe, 1 = Phishing)
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1] # Confidence score (0 to 1)

    print(f"Scanning: {url} | Score: {probability:.2f}")

    if prediction == 1:
        return jsonify({
            "status": "DANGER", 
            "message": f"Phishing Detected! ({probability*100:.0f}% confidence)", 
            "color": "#ff4d4d"
        })
    else:
        return jsonify({
            "status": "SAFE", 
            "message": "Site appears legitimate.", 
            "color": "#4caf50"
        })

if __name__ == '__main__':
    app.run(port=5000)