from PyPDF2 import PdfReader
from io import BytesIO

class PdfReader():
    def __init__():
        pass

    def extract(self, byte_stream: BytesIO) -> str:
        pdf_reader = PdfReader(byte_stream)
        resume_text = str()        
        for page in pdf_reader.pages:
            resume_text += page.extract_text()        
        return resume_text 