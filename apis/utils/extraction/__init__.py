from .pdf import PdfParser

from models import ExtractorTypes

def read_from_file(extraction_type: ExtractorTypes, byte_stream: bytes) -> str:
    extractor_options = {
        ExtractorTypes.pdf: PdfParser()
    }
    extract = extractor_options[extraction_type]
    return extract.extract(byte_stream)