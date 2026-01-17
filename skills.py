# Simple skill database
SKILLS_DB = [
    "python", "java", "machine learning", "deep learning",
    "nlp", "sql", "html", "css", "javascript", "react",
    "pandas", "numpy", "data analysis"
]

# Extract skills by keyword matching
def extract_skills(text):
    return [skill for skill in SKILLS_DB if skill in text]
