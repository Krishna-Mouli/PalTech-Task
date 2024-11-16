from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

class Recusive():
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 65, chunk_overlap=0)

    def chunk(self, text: str) -> List[str]:
        chunks = self.text_splitter.create_documents([text])
        return chunks