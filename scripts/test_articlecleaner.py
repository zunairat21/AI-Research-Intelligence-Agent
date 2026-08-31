from src.intelligence.article_cleaner import ArticleCleaner

cleaner = ArticleCleaner()
messy_text = """
    AI   research is growing.

       Models      are improving.

    Evidence   matters.
"""

expected_text = """AI research is growing.
Models are improving.
Evidence matters."""

cleaned_text = cleaner.clean(messy_text)

print("Cleaned text:")
print(cleaned_text)

print("\nExpected text:")
print(expected_text)

print("\nTest passed:", cleaned_text == expected_text)
