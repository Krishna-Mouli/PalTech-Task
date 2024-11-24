import logging
import os
import json

from ..database import TableRepository
from ..ai import OpenAIServices
from data import MemorySummarizer
from utils import Configuration, PromptTemplate
from models import ConfigurationTypes

class MemoryModule:
    def __init__(self, sourceid, convoid, resumeid):
        self.sourceid = sourceid
        self.resumeid = resumeid
        self.convo_id = convoid        
        self._memoryrepo = TableRepository(MemorySummarizer)
        self._oaiservice = OpenAIServices()
        self._prompttemplateservice = PromptTemplate()            
        self.airesponsedict = {} 
        self._config = Configuration()
        self.defaultuser = self._config.get_config_values(ConfigurationTypes.DefaultUser.value)

    async def update_or_add_summary_content(self, user_request, ai_response):
        try:
            await self._memoryrepo.init()
            summarized_content = await self.get_summerized_conversation_content(sourceid = self.sourceid, conversationid = self.convo_id, resumeid = self.resumeid)
            if summarized_content is not None:                
                summary = summarized_content['summarizedcontent']
                for_summerization_prmopt_dict = self._prompttemplateservice.create_a_prompt_template(airesponse = ai_response, user_request = user_request, 
                                                                     promptType = 'summarization', 
                                                                     previosly_summarized_content = summary)

                ai_summarization = await self._oaiservice.ChatCompletion(user_prompt=for_summerization_prmopt_dict['user_prompt'],
                                                                   system_prompt=for_summerization_prmopt_dict['system_prompt'], 
                                                                   json_mode=True,
                                                                   model = 'gpt-4o')
                ai_summary_response = json.loads(ai_summarization)
                memoryObject = MemorySummarizer(
                    PartitionKey = summarized_content['PartitionKey'],
                    RowKey = summarized_content['RowKey'],                      
                    conversationid = summarized_content['conversationid'],
                    userid = summarized_content['userid'],
                    summarizedcontent = ai_summary_response['Summary']
                )
                memory_dict = dict(memoryObject)
                await self._memoryrepo.upsert_async(memory_dict)
                logging.info("Updated memory successfully")

            else:          
                # we are going to return the new summary content                                  
                for_summerization_prmopt_dict = self._prompttemplateservice.create_a_prompt_template(airesponse = ai_response, user_request = user_request, 
                                                                     promptType = 'summarization', 
                                                                     previosly_summarized_content = None)

                ai_summarization = await self._oaiservice.ChatCompletion(user_prompt=for_summerization_prmopt_dict['user_prompt'],
                                                                   system_prompt=for_summerization_prmopt_dict['system_prompt'], 
                                                                   json_mode=True)
                ai_summary_response = json.loads(ai_summarization)

                memoryObject = MemorySummarizer(
                    PartitionKey = self.sourceid,
                    RowKey = self.resumeid,
                    conversationid = self.convo_id,
                    userid = self.defaultuser,
                    summarizedcontent = ai_summary_response['Summary']
                )
                memory_dict = dict(memoryObject)
                await self._memoryrepo.upsert_async(memory_dict)
                logging.info("Added new memory successfully")

        except Exception as e:
            logging.error('An error occured:' + str(e))
                
    async def get_summerized_conversation_content(self, sourceid, conversationid, resumeid):
        try:
            await self._memoryrepo.init()
            summarised_content_list = await self._memoryrepo.query_async(filter_query = f"PartitionKey eq '{sourceid}' and RowKey eq '{resumeid}' and conversationid eq '{conversationid}'")
            if summarised_content_list:
                summarised_content = summarised_content_list[0]
                if summarised_content:
                    return summarised_content
            else:
                return None
        except Exception as e:
            logging.error('could not get summarised content due to: ' + str(e))

    async def delete_memory(self, sourceid, resumeid):
        try:
            await self._memoryrepo.init()
            await self._memoryrepo.delete_async(partition_key = sourceid, row_key = resumeid)
            return True
        except Exception as e:
            logging.error('could not delete summarised content due to: ' + str(e))
