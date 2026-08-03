from src.storage.storage import Storage
from src.ingestion.models import AIUpdate
storage = Storage()

update1 = AIUpdate(
    title="OpenAI launches GPT-6 Research Preview",
    url="https://openai.com/blog/gpt-6-research-preview",
    summary="OpenAI introduces an early research preview of GPT-6 with improved reasoning capabilities.",
    source="OpenAI",
    category="LLM",
    date="2026-07-27"
)

update2 = AIUpdate(
    title="Anthropic releases Claude Code Studio",
    url="https://anthropic.com/news/claude-code-studio",
    summary="Anthropic announces a new coding environment powered by Claude.",
    source="Anthropic",
    category="AI Coding",
    date="2026-07-27"
)
update3 = AIUpdate(
    title="Google DeepMind unveils Gemini Robotics",
    url="https://deepmind.google/news/gemini-robotics",
    summary="Google DeepMind introduces Gemini Robotics for real-world robotic tasks.",
    source="Google DeepMind",
    category="Robotics",
    date="2026-07-28"
)

#storage.save_update(update1)
#storage.save_update(update2)
#storage.save_update(update3)

deleted_update = storage.delete_update_by_url("https://deepmind.google/news/gemini-robotics")

if deleted_update is True:

    print("Succefully deleted the required record")

else:
    print("None record is matched")
