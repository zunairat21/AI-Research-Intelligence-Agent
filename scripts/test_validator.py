from src.ingestion.validator import Validator
from src.ingestion.models import AIUpdate


validator = Validator()
valid_update = AIUpdate(
    title="GPT-5.6 Released",
    source="OpenAI",
    url="https://...",
    date="Jul 14, 2026",
    category="Product"
)

missing_title_update = AIUpdate(
    title="",
    source="OpenAI",
    url="https://...",
    date="Jul 14, 2026",
    category="Product"
)

misisng_source_update = AIUpdate(
    title="GPT-5.6 Released",
    source="",
    url="https://...",
    date="Jul 14, 2026",
    category="Product"
)

missing_url_update = AIUpdate(
    title="GPT-5.6 Released",
    source="OpenAI",
    url="",
    date="Jul 14, 2026",
    category="Product"
)

missing_date_update = AIUpdate(
    title="GPT-5.6 Released",
    source="OpenAI",
    url="https://...",
    date="",
    category="Product"
)

valid_update = validator.is_valid(valid_update)
print(f"Valid Update: {valid_update}")

valid_update = validator.is_valid(missing_title_update)
print(f"Missing title update: {valid_update}")

valid_update = validator.is_valid(misisng_source_update)
print(f"Missing source update: {valid_update}")

valid_update = validator.is_valid(missing_url_update)
print(f"Missing Url update: {valid_update}")

valid_update = validator.is_valid(missing_date_update)
print(f"Missing Date update: {valid_update}")