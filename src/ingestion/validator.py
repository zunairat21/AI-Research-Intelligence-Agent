from src.ingestion.models import AIUpdate


class Validator:   ##validator has nothing to store like collector need to store sources but validator recieves one aiupdate.

     def is_valid(self, update : AIUpdate) -> bool:
          
          if not update.title:
            return False
          if not update.source:
            return False
          if not update.url:
            return False
          if not update.date:
            return False
        
          return True
      
