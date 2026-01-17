# 🤖 AI-Powered ATS Resume Screening & Job Recommendation System

An end-to-end **AI-based Applicant Tracking System (ATS)** that analyzes resumes and job descriptions using **Natural Language Processing (NLP)** and **Machine Learning** to compute ATS scores, predict job roles, and provide career insights.

---

## 🔍 Project Overview

Recruiters use Applicant Tracking Systems (ATS) to filter resumes before interviews.  
This project simulates a real-world ATS by evaluating how well a resume matches a job description and highlighting areas for improvement.

The system provides:
- Transparent ATS score calculation
- Job role recommendations
- Skill gap analysis
- Career insights such as expected salary packages and job openings

---

## ✨ Key Features

- 📄 Upload and parse resumes in **PDF format**
- 🧠 Extract technical skills using NLP
- 🎯 Explainable **ATS Score Breakdown**:
  - Skill Match
  - Education Match
  - Project / Experience Match
- 🤖 **Machine Learning-based Job Role Prediction**
- 📊 Data-driven final ATS score using regression
- 🚀 Career insights:
  - Estimated job openings
  - Recommended skills to improve salary
  - Expected fresher salary ranges (India)
- 📄 Downloadable **ATS Analysis Report (PDF)**
- 🌐 Deployed as an interactive **Streamlit web application**

---

## 🧠 Machine Learning Techniques Used

| Task | Technique |
|---|---|
| Job Role Prediction | TF-IDF + Logistic Regression |
| ATS Score Calculation | Linear Regression |
| Skill Matching | Keyword-based NLP (Explainable) |

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Frontend / UI:** Streamlit  
- **Machine Learning:** Scikit-learn  
- **NLP:** TF-IDF Vectorization  
- **PDF Processing:** PyMuPDF  
- **Model Storage:** Joblib  
- **Report Generation:** ReportLab  

---

## ▶️ How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Train ML models (run once)
python ml_models/train_role_model.py
python ml_models/train_ats_model.py

# Run the Streamlit app
streamlit run app.py

