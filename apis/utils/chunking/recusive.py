from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from utils import Configuration
from models import ConfigurationTypes

class Recusive():
    def __init__(self):
        self._config = Configuration()
        self.chunk_size = self._config.get_config_values(ConfigurationTypes.ChunkSize.value)
        self.chunk_overlap = self._config.get_config_values(ConfigurationTypes.ChunkOverlap.value)
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size = self.chunk_size, chunk_overlap = self.chunk_overlap)

    def chunk(self, text: str) -> List[str]:
        chunks = self.text_splitter.create_documents([text])
        final_chunks = []
        for chunk in chunks:
            final_chunks.append(chunk.page_content)
        return final_chunks