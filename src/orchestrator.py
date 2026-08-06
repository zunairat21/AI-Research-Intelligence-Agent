from src.ingestion.sources.openai_source import OpenAISource
from src.ingestion.cleaner import Cleaner
from src.ingestion.validator import Validator
from src.storage.storage import Storage

class Orchestrator :

    def __init__(self):
        self.openai_source = OpenAISource()
        self.cleaner = Cleaner()
        self.validator = Validator()
        self.storage = Storage()

    def run(self):

        raw_response = self.openai_source.fetch_raw_data() 
        parsed_response = self.openai_source.parse_response(raw_response)
        aiupdates = self.openai_source.convert_to_ai_updates(parsed_response)

        save_updates = 0
        for aiupdate in aiupdates:

            if  not self.validator.is_valid(aiupdate):

                continue 
             
            cleaned_aiupdate = self.cleaner.clean(aiupdate)

            aiupdate_exist = self.storage.update_exists(cleaned_aiupdate.url)

            if aiupdate_exist:

                 continue
                
           
            self.storage.save_update(cleaned_aiupdate)

            save_updates += 1

        return save_updates

