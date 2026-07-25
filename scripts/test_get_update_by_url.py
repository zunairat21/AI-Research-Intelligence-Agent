from src.storage.storage import Storage
from src.ingestion.models import AIUpdate
storage = Storage()

##New update 

update = AIUpdate(
    title="Gemini 3.0 Released",
    source="Google DeepMind",
    url="https://deepmind.google/gemini3",
    date="2026-07-22",
    category="LLM",
    summary="Google DeepMind introduced Gemini 3.0 with improved reasoning and multimodal capabilities.",
    tags="Gemini, LLM, Google, AI"
)

storage.save_update(update)

#Case 01
update_by_url = storage.get_update_by_url("https://openai.com/")

##Case 02 
update_by_url = storage.get_update_by_url("https://deepmind.google/gemini3")

print(update_by_url)