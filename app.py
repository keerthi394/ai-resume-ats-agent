import streamlit as st
from resume_parser import extract_text_from_pdf
from skills import extract_skills
from agents import predict_job_role
from job_matcher import (
    skill_match_score,
    education_match_score,
    project_match_score,
    predict_ats_score
)
from feedback import generate_feedback
from report_generator import generate_pdf
from career_insights import get_career_insights

st.set_page_config(page_title="AI ATS Resume Analyzer")

st.title("🤖 AI Resume Screening & Job Recommendation Agent")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if resume_file and job_description:

        # ---------- TEXT EXTRACTION ----------
        resume_text = extract_text_from_pdf(resume_file)
        job_text = job_description.lower()

        # ---------- SKILL EXTRACTION ----------
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_text)

        # ---------- ATS SUB-SCORES ----------
        skill = skill_match_score(resume_skills, job_skills)
        edu = education_match_score(resume_text)
        proj = project_match_score(resume_text)

        # ---------- FINAL ATS SCORE (ML) ----------
        final_score = predict_ats_score(skill, edu, proj)

        # ---------- JOB ROLE PREDICTION ----------
        role = predict_job_role(resume_text)

        # ---------- FEEDBACK ----------
        feedback = generate_feedback(
            list(set(job_skills) - set(resume_skills)),
            final_score
        )

        # ---------- UI OUTPUT ----------
        st.subheader("🎯 ATS Score Breakdown")

        st.markdown(f"### 🧠 Skill Match — {skill}%")
        st.progress(skill / 100)

        st.markdown(f"### 🎓 Education Match — {edu}%")
        st.progress(edu / 100)

        st.markdown(f"### 🛠️ Project / Experience Match — {proj}%")
        st.progress(proj / 100)

        st.success(f"✅ Final ATS Score: {final_score}%")
        st.write(f"🎯 **Recommended Role:** {role}")

        # ---------- CAREER INSIGHTS ----------
        st.subheader("🚀 Career Insights")

        insights = get_career_insights(role)
        if insights:
            st.write(f"📌 **Current Job Openings:** {insights['openings']}")
            st.write(f"💰 **Expected Package:** {insights['package']}")
            st.write("🧠 **Skills to Improve for Higher Package:**")
            for s in insights["skills_to_improve"]:
                st.write(f"• {s}")

        # ---------- RESUME FEEDBACK ----------
        st.subheader("📌 Resume Feedback")
        for f in feedback:
            st.write("•", f)

        # ---------- PDF DOWNLOAD ----------
        if st.button("📄 Download ATS Report (PDF)"):
            pdf_file = generate_pdf(
                final_score, role, skill, edu, proj, feedback
            )
            with open(pdf_file, "rb") as f:
                st.download_button(
                    "⬇️ Download Report",
                    f,
                    file_name="ATS_Report.pdf",
                    mime="application/pdf"
                )
