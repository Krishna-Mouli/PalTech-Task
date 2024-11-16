from .recusive import Recusive
from typing import List
from models import ChunkingTypes

def chunk_content(chunking_type: ChunkingTypes, text: str) -> List[str]:
    chunking_options = {
        ChunkingTypes.Recursive: Recusive()
    }
    chunking = chunking_options[chunking_type]
    return chunking.chunk(text)