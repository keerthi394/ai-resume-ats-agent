def generate_feedback(missing_skills, score):
    feedback = []
    if missing_skills:
        feedback.append(f"Learn missing skills: {', '.join(missing_skills)}")
    if score < 60:
        feedback.append("Add more relevant projects")
    if not feedback:
        feedback.append("Resume is well optimized for ATS")
    return feedback
