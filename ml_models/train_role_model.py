import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

os.makedirs("models", exist_ok=True)

data = {
    "text": [
        "python machine learning nlp",
        "html css javascript react",
        "sql pandas numpy data analysis",
        "deep learning model training",
        "frontend web development",
        "data visualization sql pandas"
    ],
    "role": [
        "ML Engineer",
        "Web Developer",
        "Data Analyst",
        "ML Engineer",
        "Web Developer",
        "Data Analyst"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["text"])
y = df["role"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump((vectorizer, model), "models/role_model.pkl")
print("✅ Role model trained")
