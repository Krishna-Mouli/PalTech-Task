import logging
from openai import AsyncOpenAI as OpenAI
from utils import Configuration
from models import ConfigurationTypes

class OpenAIServices:
    def __init__(self):
        self._config = Configuration()
        self.api_key = self._config.get_config_values(ConfigurationTypes.OpenaiApiKey)
        self.openai_client = OpenAI(api_key = self.api_key)
        self.openai_model = self._config.get_config_values(ConfigurationTypes.OpenAIModel)
        logging.info("OpenAI API Key set to: " + self.api_key)
        
    async def ChatCompletion(self, user_prompt, system_prompt, model=None, json_mode: bool = False):
        try:
            if model is None:
                model = self.openai_model
            # Base parameters
            params = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
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
            model = self.openai_model
        if dimensions is None:
            dimensions = int(os.environ.get("DefaultOutPutVectorDimensions"))
        response = await self.openai_client.embeddings.create(
            model=model,
            input=text,
            encoding_format="float",
            dimensions=dimensions
        )
        return response.data[0].embedding