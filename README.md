# 🛡️ FinShield – AI-Powered Phishing Detection Extension

> A lightweight Chrome extension powered by Machine Learning that helps users identify potentially malicious or phishing websites before interacting with them.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-green?logo=googlechrome)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## 📖 Overview

Phishing attacks are one of the most common cybersecurity threats, often tricking users into revealing sensitive information through fake websites.

**FinShield** combines a Chrome Extension with a Machine Learning backend to analyze the currently opened webpage and determine whether it is likely to be a phishing website. Instead of relying solely on blacklists, it predicts the legitimacy of URLs using extracted URL-based features.

---

## ✨ Features

- 🔍 Real-time URL scanning
- 🤖 Machine Learning-based phishing detection
- 🌐 Chrome Extension for seamless browser integration
- ⚡ Instant Safe/Danger classification
- 📊 Confidence-based predictions
- 🔒 Lightweight and easy to deploy

---

## 🏗️ Architecture

```text
                User Opens Website
                        │
                        ▼
             Chrome Extension Popup
                        │
              Reads Current Tab URL
                        │
                        ▼
              Flask Backend API
               (/scan endpoint)
                        │
              Feature Extraction
                        │
                        ▼
          Trained ML Phishing Model
                        │
              Safe / Danger Result
                        │
                        ▼
           Displayed in Extension
```

---

## 🧠 Machine Learning Pipeline

The backend extracts several URL characteristics before making a prediction.

Current features include:

- URL length
- Number of dots (`.`)
- Number of hyphens (`-`)
- Number of `@` symbols
- Presence of an IP address
- HTTPS usage

These features are fed into the trained phishing detection model (`phishing_model.pkl`) to classify the website.

---

## 📂 Project Structure

```
FinShield/
│
├── backend/
│   ├── app.py                  # Flask API
│   ├── train_model.py          # Model training script
│   ├── phishing_model.pkl      # Trained ML model
│   └── req.txt                 # Python dependencies
│
└── extensions/
    ├── manifest.json           # Chrome Extension manifest
    ├── popup.html
    ├── popup.js
    └── icon.png
```

---

## ⚙️ Tech Stack

### Frontend
- Chrome Extension (Manifest V3)
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### Machine Learning
- NumPy
- Joblib
- Scikit-learn

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ishanyawhocares/finShield.git

cd finShield
```

---

### 2. Install backend dependencies

```bash
cd backend

pip install -r req.txt
```

If required:

```bash
pip install numpy joblib scikit-learn
```

---

### 3. Start the Flask server

```bash
python app.py
```

The server starts on:

```
http://127.0.0.1:5000
```

---

### 4. Load the Chrome Extension

1. Open Chrome.
2. Navigate to:

```
chrome://extensions/
```

3. Enable **Developer Mode**.
4. Click **Load unpacked**.
5. Select the `extensions` folder.

---

### 5. Test the extension

Open any website and click the FinShield extension.

The extension will:

- Read the current URL
- Send it to the Flask backend
- Analyze it using the ML model
- Display whether the website is:

✅ SAFE

or

🚨 DANGER

---

## 📡 API

### POST `/scan`

Scans a URL using the trained ML model.

### Request

```json
{
    "url": "https://example.com"
}
```

### Safe Response

```json
{
    "status": "SAFE",
    "message": "Site appears legitimate.",
    "color": "#4caf50"
}
```

### Phishing Response

```json
{
    "status": "DANGER",
    "message": "Phishing Detected! (95% confidence)",
    "color": "#ff4d4d"
}
```

---

## 🔒 Why FinShield?

Unlike traditional blacklist-based solutions, FinShield leverages Machine Learning to identify suspicious URL patterns, enabling it to detect previously unseen phishing attempts based on learned characteristics.

---

## 📈 Future Improvements

- URL reputation services integration
- Domain age analysis
- WHOIS lookup
- SSL certificate validation
- Google Safe Browsing API
- Deep Learning models
- Real-time page content analysis
- Email phishing detection
- Browser warning page before navigation
- Cloud deployment

---

## 📸 Demo

You can add screenshots here.

```
assets/
├── popup.png
├── detection.png
└── safe.png
```

Example:

```markdown
![Extension Popup](assets/popup.png)
```

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Ishanya Sharma**

- GitHub: https://github.com/ishanyawhocares

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project!
