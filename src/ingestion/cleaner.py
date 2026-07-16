from src.ingestion.models import AIUpdate


class Cleaner:

    def clean(self, update: AIUpdate) -> AIUpdate:

        update.title = update.title.strip()
        update.source = update.source.strip()
        update.date = update.date.strip()
        update.url = update.url.strip()

        if  update.category:
            
           update.category = update.category.strip()
        return update
    

        

