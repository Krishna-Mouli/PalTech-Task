from data import Vectors
from typing import Dict

class DataHelpers:
    def __init__(self):
        pass

    def createvectorsdict(self, vectors_user_request) -> Dict[str, Vectors]:
        vector_dict: Dict[str, Vectors] = {}
        for vector in vectors_user_request:        
            vector_obj = Vectors(
                vector_id = vector['id'],
                chunk_content = vector['metadata']['chunk_content'],
                resumeid = vector['metadata']['resumeid'],
                sourceid = vector['metadata']['sourceid'],
                filename = vector['metadata']['filename'],
                filepath = vector['metadata']['filepath'],
                score = vector['score'],
                values = vector['values']
            )        
            vector_dict[vector['id']] = vector_obj
        return vector_dict