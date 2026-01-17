from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(score, role, skill, edu, proj, feedback):
    file_name = "ATS_Report.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "AI ATS Resume Analysis Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Final ATS Score: {score}%")
    c.drawString(50, 740, f"Recommended Role: {role}")

    c.drawString(50, 700, f"Skill Match: {skill}%")
    c.drawString(50, 680, f"Education Match: {edu}%")
    c.drawString(50, 660, f"Project Match: {proj}%")

    c.drawString(50, 620, "Feedback:")
    y = 600
    for f in feedback:
        c.drawString(70, y, f"- {f}")
        y -= 20

    c.save()
    return file_name
