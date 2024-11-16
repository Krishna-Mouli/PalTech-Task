from .pdf import PdfReader

from models import ExtractorTypes

def read_from_file(extraction_type: ExtractorTypes, byte_stream: bytes) -> str:
    extractor_options = {
        ExtractorTypes.pdf: PdfReader()
    }
    extract = extractor_options[extraction_type]
    return extract.extract(byte_stream)