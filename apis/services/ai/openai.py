import logging
from openai import AsyncOpenAI as OpenAI
from utils import Configuration
from models import ConfigurationTypes

class OpenAIServices:
    def __init__(self):
        self._config = Configuration()
        self.api_key = self._config.get_config_values(ConfigurationTypes.OpenaiApiKey.value)
        self.openai_client = OpenAI(api_key = self.api_key)             
        logging.info("OpenAI API Key set to: " + self.api_key)
        
    async def ChatCompletion(self, user_prompt, system_prompt, model=None, json_mode: bool = False):
        try:
            if model is None:
                model = self._config.get_config_values(ConfigurationTypes.OpenAIModel.value)             
            params = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature":0.2,
                "max_tokens":2009,
                "top_p":1,
                "frequency_penalty":0,
                "presence_penalty":0,                
            }           
            if json_mode:
                params["response_format"] = {"type": "json_object"}
            response = await self.openai_client.chat.completions.create(**params)
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Error occurred while creating chat completion: {str(e)}")
            raise
    
    async def EmbeddingsOpenAI(self,text,model=None,dimensions=None):
        if model is None:
            model = self._config.get_config_values(ConfigurationTypes.EmbeddingModel.value)
        if dimensions is None:
            dimensions = self._config.get_config_values(ConfigurationTypes.VectorDimensions.value)
        response = await self.openai_client.embeddings.create(
            model=model,
            input=text,
            encoding_format="float",
            dimensions=dimensions
        )
        return response.data[0].embedding