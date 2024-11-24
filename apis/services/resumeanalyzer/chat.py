import logging
from utils import PromptTemplate, DataHelpers
from ..ai import OpenAIServices
from ..database import PineConeService
from ..memorymodule import MemoryModule

class Chat():
    def __init__(self, resumeid, convoid, sourceid):
        self._openaiservice = OpenAIServices()
        self._pineconeservice = PineConeService()
        self._prompttemplate = PromptTemplate()  
        self._memorymodule = MemoryModule(resumeid = resumeid, convoid = convoid, sourceid = sourceid)      
        self._datahelper = DataHelpers()

    async def converse_init(self, convo_id: str, resumeid: str, question: str, sourceid: str):
        summarized_conversation_history = await self._memorymodule.get_summerized_conversation_content(sourceid = sourceid, conversationid = convo_id, resumeid = resumeid)
        summary_string = "" if summarized_conversation_history is None else summarized_conversation_history        
        vectors_user_request = await self._openaiservice.EmbeddingsOpenAI(text = question)
        similar_vectors = self._pineconeservice.get_vectors(target_vectors = vectors_user_request, resumeid = resumeid)
        vectors_dict = self._datahelper.createvectorsdict(similar_vectors) 
        multicontext_prompt_dict = self._prompttemplate.create_a_prompt_template(vectors = vectors_dict,
                                                                                user_request = question, 
                                                                                promptType='infercontext',
                                                                                previosly_summarized_content = summary_string)
        response = await self._openaiservice.ChatCompletion(user_prompt=multicontext_prompt_dict["user_prompt"], 
                                                         system_prompt=multicontext_prompt_dict["system_prompt"])
        await self._memorymodule.update_or_add_summary_content(ai_response = response, user_request = question)
        return response
    
    async def reset_conversation(self, resumeid: str, sourceid: str):
        try:
            status = await self._memorymodule.delete_memory(sourceid = sourceid, resumeid = resumeid)
            if(status == True):
                return status
            else:
                return False
        except Exception as e:
            logging.error(f"{str(e)}")