from src.storage.storage import Storage
from src.ingestion.models import AIUpdate

storage = Storage()

update1 = AIUpdate(
    title="Meta Introduces Llama 5",
    source="Meta AI",
    url="https://example.com/meta/llama5-launch",
    date="2026-08-05",
    category="LLM",
    summary="Meta announced Llama 5 with enhanced multilingual capabilities.",
    tags="Meta,Llama5,LLM,AI"
)

update2 = AIUpdate(
    title="Microsoft Releases Phi-5",
    source="Microsoft Research",
    url="https://example.com/microsoft/phi5-release",
    date="2026-08-06",
    category="Small Language Model",
    summary="Microsoft unveiled Phi-5 optimized for efficient on-device AI.",
    tags="Microsoft,Phi5,SLM,AI"
)

storage.save_update(update1)
storage.save_update(update2)

update1.title = "Meta Launches Llama 5.1"
update1.summary = "Meta released Llama 5.1 with improved reasoning and coding performance."
update1.category = "Foundation Model"

storage.update_aiupdate(update1)
storage.update_aiupdate(update1)
updated_ai_update = storage.update_aiupdate(update1)

print(updated_ai_update)




ai_update = storage.get_update_by_url("https://example.com/meta/llama5-launch")

print(ai_update)

