from src.storage.storage import Storage
from src.ingestion.models import AIUpdate

storage = Storage()

update1 = AIUpdate(
    title="GPT-5.6 Released",
    source="OpenAI",
    url="https://example.com/anthropic/claude-5-test1",
    date="2026-07-20",
    category="LLM",
    summary="OpenAI released GPT-5.6 with improved reasoning.",
    tags="GPT-5.6,LLM,OpenAI"
)

update2 = AIUpdate(
    title="OpenAI Voice Agent",
    source="OpenAI",
    url="https://example.com/openai/voice-agent-test1",
    date="2026-07-21",
    category="AI Agent",
    summary="OpenAI introduced a new voice AI agent.",
    tags="Voice,Agent,OpenAI"
)

update3 = AIUpdate(
    title="Claude 5 Released",
    source="Anthropic",
    url="https://example.com/openai/gpt-5-6-test1",
    date="2026-07-22",
    category="LLM",
    summary="Anthropic announced Claude 5.",
    tags="Claude,Anthropic,LLM"
)

storage.save_update(update1)
storage.save_update(update2)
storage.save_update(update3)

updates = storage.get_updates_by_source("Anthropic")


assert updates[0].source == "Anthropic"
