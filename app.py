import gradio as gr
from services.parser_service import extract_text
from services.ai_service import analyze_resume
from services.report_service import generate_pdf_report
from services.chart_service import generate_chart


def process_resume(file, role, resume_text):
    text = resume_text.strip() if resume_text else ''
    if file is not None:
        text = extract_text(file.name)
    if not text:
        return {'error': 'No resume text found'}, None, None
    result = analyze_resume(text, role)
    chart = generate_chart(result.get('scores', {}))
    pdf = generate_pdf_report(result)
    return result, chart, pdf

with gr.Blocks(css='assets/style.css') as demo:
    gr.Markdown('# 🚀 AI Resume Analyzer')
    with gr.Row():
        with gr.Column():
            file = gr.File(label='Upload Resume PDF/DOCX')
            resume_text = gr.Textbox(lines=14, label='Or Paste Resume Text')
            role = gr.Dropdown(['AI/ML Engineer','Data Scientist','Software Engineer','Python Developer'], value='AI/ML Engineer', label='Target Role')
            btn = gr.Button('Analyze Resume')
        with gr.Column():
            output = gr.JSON(label='Analysis')
            chart = gr.Image(label='Score Chart')
            pdf = gr.File(label='Download PDF Report')
    btn.click(process_resume, [file, role, resume_text], [output, chart, pdf])

demo.launch(
    server_name='127.0.0.1', 
    server_port=7860,
    share=True)