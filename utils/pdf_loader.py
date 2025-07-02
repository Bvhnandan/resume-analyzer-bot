# utils/pdf_loader.py
from PyPDF2 import PdfReader

def load_resume_text(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.strip()
