import joblib
import pandas as pd

# ---------- Explainable Sub-Scores ----------

def skill_match_score(resume_skills, job_skills):
    if not job_skills:
        return 50
    return round(len(set(resume_skills) & set(job_skills)) / len(job_skills) * 100, 2)

def education_match_score(resume_text):
    keywords = ["b.tech", "bachelor", "engineering", "computer science"]
    return 80 if any(k in resume_text for k in keywords) else 40

def project_match_score(resume_text):
    keywords = ["project", "internship", "application"]
    return 80 if any(k in resume_text for k in keywords) else 40

# ---------- ML-Based Final ATS Score ----------

ats_model = joblib.load("models/ats_model.pkl")

def predict_ats_score(skill, edu, project):
    data = pd.DataFrame([[skill, edu, project]],
                        columns=["skill_score", "edu_score", "project_score"])
    return round(ats_model.predict(data)[0], 2)
