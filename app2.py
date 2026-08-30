import gradio as gr
from services.parser_service import extract_text
from services.ai_service import analyze_resume
from services.report_service import generate_pdf_report
from services.chart_service import generate_chart


def process_resume(file, role, resume_text):
    text = resume_text.strip() if resume_text else ""

    if file is not None:
        text = extract_text(file.name)

    if not text:
        return {"error": "Please upload a file or paste resume text."}, None, None

    result = analyze_resume(text, role)
    chart_path = generate_chart(result.get("scores", {}))
    pdf_path = generate_pdf_report(result)

    return result, chart_path, pdf_path


with gr.Blocks(theme=gr.themes.Soft(), title="AI Resume Analyzer") as demo:

    gr.Markdown("""
# 🚀 AI Resume Analyzer
### Modern ATS + AI Resume Review Dashboard
Upload a resume or paste text, choose a role, and generate instant feedback.
""")

    with gr.Row(equal_height=True):

        with gr.Column(scale=1, min_width=360):
            gr.Markdown("## 📥 Input")

            resume_file = gr.File(
                label="Upload Resume (PDF / DOCX)",
                file_count="single"
            )

            resume_text = gr.Textbox(
                label="Or Paste Resume Text",
                lines=14,
                placeholder="Paste resume text here..."
            )

            role = gr.Dropdown(
                choices=[
                    "AI/ML Engineer",
                    "Data Scientist",
                    "Software Engineer",
                    "Python Developer",
                    "NLP Engineer"
                ],
                value="AI/ML Engineer",
                label="Target Role"
            )

            analyze_btn = gr.Button("Analyze Resume", variant="primary")
            clear_btn = gr.ClearButton(
                components=[resume_file, resume_text],
                value="Clear"
            )

        with gr.Column(scale=2):
            gr.Markdown("## 📊 Results")

            with gr.Tabs():

                with gr.Tab("Analysis"):
                    output_json = gr.JSON(label="Structured Result")

                with gr.Tab("Chart"):
                    output_chart = gr.Image(label="Scores Chart")

                with gr.Tab("Report"):
                    output_pdf = gr.File(label="Download PDF Report")

    analyze_btn.click(
        fn=process_resume,
        inputs=[resume_file, role, resume_text],
        outputs=[output_json, output_chart, output_pdf]
    )

demo.launch(
    server_name="127.0.0.1",
    server_port=7860
)