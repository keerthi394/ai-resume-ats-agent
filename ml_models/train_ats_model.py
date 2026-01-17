import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
import os

os.makedirs("models", exist_ok=True)

data = {
    "skill_score": [90, 70, 60, 80, 50],
    "edu_score": [80, 70, 90, 60, 50],
    "project_score": [85, 60, 70, 90, 40],
    "final_score": [88, 68, 72, 82, 48]
}

df = pd.DataFrame(data)

X = df[["skill_score", "edu_score", "project_score"]]
y = df["final_score"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "models/ats_model.pkl")
print("✅ ATS model trained")
