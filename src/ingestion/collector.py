from typing import List
from src.ingestion.models import AIUpdate 

class Collector:

    """
    Collect AIupdates from sources
    """
    
    def __init__(self, sources):
         
        self.sources = sources

    def collect(self) ->List[AIUpdate]:

        all_updates = []

        for source in self.sources:
         try:

              response = source.fetch_raw_data()
              parsed_updates = source.parse_response(response)
              ai_updates = source.convert_to_ai_updates(parsed_updates)
              all_updates.extend(ai_updates)
         except Exception as e:

            "Handle error"

            print(f"Failed to collect updates from {source}: {e}")
        
        return all_updates