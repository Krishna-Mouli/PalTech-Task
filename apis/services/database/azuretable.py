from azure.data.tables.aio import TableServiceClient, TableClient
from azure.data.tables import UpdateMode
from azure.core.exceptions import ResourceNotFoundError
from utils import Configuration
from models import ConfigurationTypes
import logging

class TableRepository:
    def __init__(self, entity_type):
        _config = Configuration()
        self.table_name = f"{entity_type.__name__}sPALTECH"
        self.conn_str = _config.get_config_values(ConfigurationTypes.ConnectionString.value)
        service_client = TableServiceClient.from_connection_string(self.conn_str)
        self.client = service_client.get_table_client(table_name=self.table_name)
        
    async def init(self):
        """
        Creates the table asynchronously if it doesn't already exist.
        """
        try:
            await self.client.create_table()
            logging.info(f"Table '{self.table_name}' created successfully.")
        except Exception as e:
            logging.info(f"Table already exists or error creating table: {e}")

    async def get_all_async(self):
        """
        Retrieve all entities from the table asynchronously.
        """
        entities = []
        async for entity in self.client.list_entities():
            entities.append(entity)
        return entities

    async def upsert_async(self, entity):
        """
        Upsert an entity into the table asynchronously.
        """
        try:
            await self.client.upsert_entity(entity, mode=UpdateMode.MERGE)
            return await self.get_async(entity['PartitionKey'], entity['RowKey'])
        except Exception as e:
            logging.error(f"{str(e)}")

    async def get_async(self, partition_key, row_key):
        """
        Retrieve a specific entity from the table asynchronously.
        """
        try:
            entity = await self.client.get_entity(partition_key, row_key)
            return entity
        except ResourceNotFoundError:
            logging.warning(f"Entity not found for PartitionKey: {partition_key}, RowKey: {row_key}")
            return None

    async def delete_all_async(self):
        """
        Delete all entities in the table asynchronously.
        """
        async for entity in self.client.list_entities():
            await self.client.delete_entity(partition_key=entity["PartitionKey"], row_key=entity["RowKey"])
        logging.info("All entities deleted from the table.")

    async def query_async(self, filter_query: str):
        """
        Queries the Azure Table Storage asynchronously based on the provided filter.

        :param filter_query: The OData filter query string to filter entities.
        :return: A list of matching entities.
        """
        try:
            entities = []
            async for entity in self.client.query_entities(query_filter=filter_query):
                entities.append(entity)
            return entities
        except Exception as e:
            logging.error(f"Error querying entities: {str(e)}")
            return []
