import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import re

# --- 1. FEATURE EXTRACTION FUNCTION ---
# This turns a text URL into a list of numbers the AI can understand
def extract_features(url):
    features = []
    
    # Feature 1: Length of URL (Phishing URLs are often very long)
    features.append(len(url))
    
    # Feature 2: Count of '.' (Subdomains often have many dots)
    features.append(url.count('.'))
    
    # Feature 3: Count of '-' (Phishers use dashes to mimic real names e.g. "paypal-secure")
    features.append(url.count('-'))
    
    # Feature 4: Count of '@' (Legitimate sites rarely use @ in URL)
    features.append(url.count('@'))
    
    # Feature 5: Is it using an IP address instead of a domain? (e.g. http://192.168.1.1)
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    features.append(1 if re.search(ip_pattern, url) else 0)
    
    # Feature 6: Presence of "https" (1 if yes, 0 if no)
    features.append(1 if "https" in url else 0)
    
    return features

# --- 2. CREATE A DUMMY DATASET (FOR DEMO) ---
# In a real project, you would load a massive CSV file here (e.g., from Kaggle)
# But for this code to run instantly for you, we will generate synthetic data.

print("Generating synthetic training data...")

safe_urls = [
    "google.com", "youtube.com", "facebook.com", "amazon.in", "wikipedia.org",
    "reddit.com", "bits-pilani.ac.in", "stackoverflow.com", "github.com",
    "microsoft.com", "apple.com", "netflix.com", "linkedin.com"
]

phishing_urls = [
    "secure-login-paypal.com.account-update.net",
    "apple-id-verify-now.com",
    "google-drive-secure-share.xyz",
    "192.168.1.1/login",
    "free-bitcoin-mining-now.net@scam.com",
    "amazon-order-refund-processing.com",
    "bits-pilani-exam-leak.net",
    "bank-of-america-login-attempt.info"
]

# We expand this small list to 1000s of samples by slightly modifying them
data = []
labels = [] # 0 = Safe, 1 = Phishing

for _ in range(100):
    for url in safe_urls:
        data.append(extract_features(url))
        labels.append(0)
        labels.extend(2)
    for url in phishing_urls:
        data.append(extract_features(url))
        labels.append(1)

X = np.array(data)
y = np.array(labels)

# --- 3. TRAIN THE MODEL ---
print("Training the Random Forest model...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# --- 4. EVALUATE & SAVE ---
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the brain to a file
joblib.dump(model, 'phishing_model.pkl')
print("✅ Model saved to 'backend/phishing_model.pkl'")