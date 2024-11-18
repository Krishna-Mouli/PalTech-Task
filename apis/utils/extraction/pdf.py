from PyPDF2 import PdfReader
import logging
from io import BytesIO

class PdfParser():
    def __init__(self):
        pass

    def extract(self, byte_stream: bytes) -> str:
        try:
            byte_stream = BytesIO(byte_stream)
            pdf_reader = PdfReader(byte_stream)
        except Exception as e:
            logging.error(f"{str(e)}")
            return ""
        resume_text = str()        
        for page in pdf_reader.pages:
            resume_text += page.extract_text()        
        return resume_text 