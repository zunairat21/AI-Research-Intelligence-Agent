from src.ingestion.models import AIUpdate
from src.ingestion.cleaner import Cleaner

cleaner = Cleaner()

update = AIUpdate(
    title="   GPT-5.6 Released  ",
    source="  OpenAI",
    url="https://...         ",
    date="  Jul 14, 2026",
    category="                  Product"
)

cleaned_update = cleaner.clean(update)

print(f"Clean Update :{cleaned_update}")
print(cleaned_update.title)
print(cleaned_update.source)
print(cleaned_update.url)
print(cleaned_update.date)
print(cleaned_update.category)
