from enum import Enum

class ConfigurationTypes(Enum):
    ConnectionString = "connectionstring"
    ContainerName = "containername"
    PineconeKey = "pineconekey"
    PineconeIndex = "pineconeindex"
    ChunkStatagy = "chunkstatagy"
    ChunkSize = "chunksize"
    ChunkOverlap = "chunkoverlap"
    OpenaiApiKey = "openaiapikey"
    PineconeNamespace = "pineconenamespace"
    OpenAIModel = "openaimodel"
    EmbeddingModel = "embeddingmodel"
    VectorDimensions = "vectordimensions"
    DefaultUser = "defaultuser"