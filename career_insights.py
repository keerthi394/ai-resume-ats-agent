# Purpose:
# Provide career-level insights like:
# - Current job openings (approx)
# - Skills to improve salary
# - Expected fresher package (India)

CAREER_DATA = {
    "ML Engineer": {
        "openings": "15,000+",
        "skills_to_improve": [
            "Pandas", "NumPy", "Scikit-learn",
            "Deep Learning", "TensorFlow", "SQL"
        ],
        "package": "₹6 – 10 LPA (Fresher)"
    },
    "Data Analyst": {
        "openings": "20,000+",
        "skills_to_improve": [
            "Advanced SQL", "Power BI", "Tableau",
            "Statistics", "Excel"
        ],
        "package": "₹4 – 8 LPA (Fresher)"
    },
    "Web Developer": {
        "openings": "30,000+",
        "skills_to_improve": [
            "Node.js", "MongoDB", "System Design",
            "Next.js", "TypeScript"
        ],
        "package": "₹4 – 7 LPA (Fresher)"
    }
}

def get_career_insights(role):
    return CAREER_DATA.get(role, None)
