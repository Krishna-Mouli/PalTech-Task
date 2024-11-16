from config import load_config

class Configuration():
    def __init__(self):
        self.local_config = load_config("local")
        self.key_mapping = {
            "connectionstring": "database.connectionstrng",
            "containername": "database.containername",
            "pineconekey":"vectorstore.pineconekey",  
            "pineconeindex":"vectorstore.pineconeindex",
            "pineconenamespace":"vectorstore.pineconenamespace",
            "chunkstatagy":"chunking.chunkstatagy",
            "chunksize":"chunking.chunksize",
            "chunkoverlap":"chunking.chunkoverlap",
            "openaiapikey":"openai.key",   
            "openaimodel":"openai.model",
            "vectordimensions":"openai.vectordimensions",   
            "embeddingmodel":"openai.embeddingmodel"  
        }

    def get_config_values(self, config_key):       
        full_key = self.key_mapping.get(config_key)       
        if not full_key:
            raise KeyError(f"Config key '{config_key}' not found in key mapping.")        
        keys = full_key.split(".")
        value = self.local_config        
        try:
            for key in keys:
                value = value[key]
            return value
        except KeyError:
            raise KeyError(f"Config key '{full_key}' not found in the configuration.")

