from pinecone import Pinecone
from utils import Configuration
from models import ConfigurationTypes

class PineConeService:
    def __init__(self):
        self._config = Configuration()
        self.api_key = self._config.get_config_values(ConfigurationTypes.PineconeKey)
        self.pc = Pinecone(api_key = self.api_key)
        self.pineconeindex = self._config.get_config_values(ConfigurationTypes.PineconeIndex)
        self.index = self.pc.Index(self.pineconeindex)
        self.namespace = self._config.get_config_values(ConfigurationTypes.PineconeNamespace)

    def upsert_vectors(self, vectors):
        try:
            self.index.upsert(
                vectors = vectors,
                namespace= self.namespace
            )
        except Exception as e:
            print(f"Failed to upsert {e}")

    def get_vectors(self, target_vectors, app_id: str):
        try:
            response = self.index.query(
            namespace = self.namespace,
            vector = target_vectors,
            top_k = 2,
            include_values = True,
            include_metadata = True,
            filter={"appid": {"$eq": app_id}}
            )
            return (response.matches)
        except Exception as e:
            print(f"Failed to fetch data due to {e}") 