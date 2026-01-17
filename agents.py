import joblib

# Load trained role prediction model
vectorizer, model = joblib.load("models/role_model.pkl")

# Predict job role using ML
def predict_job_role(resume_text):
    X = vectorizer.transform([resume_text])
    return model.predict(X)[0]
