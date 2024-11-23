from azure.storage.blob.aio import BlobServiceClient, ContainerClient, BlobClient
from utils import Configuration
from models import ConfigurationTypes
import logging

class AzureBlobServices():
    def __init__(self):
        _config = Configuration()
        self.connection_string = _config.get_config_values(ConfigurationTypes.ConnectionString.value)
        self.container_name = _config.get_config_values(ConfigurationTypes.ContainerName.value)
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        self.container_client = self.blob_service_client.get_container_client(self.container_name)

    async def init(self):
        """
        Creates the container asynchronously if it doesn't already exist.
        """
        try:
            await self.container_client.create_container()
            logging.info(f"Container '{self.container_name}' created successfully.")
        except Exception as e:
            logging.error(f"Container already exists or could not be created: {e}")        

    async def upload_file(self, resumeid, blob_name, file_stream) -> str:        
        blob_client = self.container_client.get_blob_client(blob_name) 
        await blob_client.upload_blob(file_stream, overwrite=True)  
        blob_url = blob_client.url      
        logging.info(f"File stream uploaded to blob {blob_name} in container {self.container_name}.")
        return blob_url