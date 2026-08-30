import PyPDF2, docx

def extract_text(path):
    if path.lower().endswith('.pdf'):
        text=''
        reader=PyPDF2.PdfReader(path)
        for p in reader.pages:
            text += p.extract_text() or ''
        return text
    if path.lower().endswith('.docx'):
        d=docx.Document(path)
        return '\n'.join([p.text for p in d.paragraphs])
    return ''