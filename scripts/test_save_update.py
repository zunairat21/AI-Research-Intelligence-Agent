from src.storage.storage import Storage
from src.ingestion.models import AIUpdate
storage = Storage()

update = AIUpdate(
    title="GPT-5.6 Released",
        source="OpenAI",
        url="https://...",
        date="",
        category="Product",
        summary = None,
        tags = None
)

storage.save_update(update) ## As in save_update it is saving in database nothing is returning no need to assign it to any variable 

updates = storage.get_all_updates()

for update in updates:
    print(update) ##No parameter required as it is reading from sql 



