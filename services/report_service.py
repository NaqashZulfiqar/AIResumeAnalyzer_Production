import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(data):
    os.makedirs('outputs/reports', exist_ok=True)
    file='outputs/reports/resume_report.pdf'
    pdf=SimpleDocTemplate(file)
    styles=getSampleStyleSheet()
    story=[Paragraph('AI Resume Report', styles['Title']), Spacer(1,12)]
    for k,v in data.items():
        story.append(Paragraph(f'<b>{k}</b>: {v}', styles['Normal']))
        story.append(Spacer(1,8))
    pdf.build(story)
    return file