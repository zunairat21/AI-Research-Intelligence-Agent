from src.storage.storage import Storage
from src.ingestion.models import AIUpdate

storage = Storage()
update1 = AIUpdate(
    title="GPT-5.6 Released",
    source="OpenAI",
    url="https://example.com/test/gpt56",
    date="2026-07-20",
    category="LLM",
    summary="OpenAI released GPT-5.6.",
    tags="GPT-5.6,LLM,OpenAI"
)

update2 = AIUpdate(
    title="Claude 5 Released",
    source="Anthropic",
    url="https://example.com/test/claude5",
    date="2026-07-21",
    category="LLM",
    summary="Anthropic announced Claude 5.",
    tags="Claude5,LLM,Anthropic"
)

update3 = AIUpdate(
    title="OpenAI Voice Agent",
    source="OpenAI",
    url="https://example.com/test/voiceagent",
    date="2026-07-22",
    category="AI Agent",
    summary="OpenAI launched a voice AI agent.",
    tags="Voice,Agent,OpenAI"
)

storage.save_update(update1)
storage.save_update(update2)
storage.save_update(update3)

updates = storage.get_updates_by_category("LLM")

assert updates[0].category == "LLM"

print(updates)