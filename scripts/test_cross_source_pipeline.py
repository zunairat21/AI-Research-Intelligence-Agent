from src.intelligence.article_cleaner import ArticleCleaner
from src.intelligence.article_extractor import ArticleExtractor
from src.intelligence.article_fetcher import ArticleFetcher


fetcher = ArticleFetcher()
extractor = ArticleExtractor()
cleaner = ArticleCleaner()

test_cases = {
    "OpenAI": (
        "https://openai.com/index/"
        "bringing-chatgpt-for-teachers-to-more-us-school-districts/"
    ),
    "Anthropic": (
        "https://www.anthropic.com/research/riemann-zeta"
    ),
    "DeepMind": (
        "https://deepmind.google/blog/"
        "from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/"
    ),
}

for source, url in test_cases.items():
    raw_html = fetcher.fetch(url)

    article_content = extractor.extract(
        raw_html,
        source
    )

    cleaned_article = cleaner.clean(article_content)

    print("\n" + "=" * 70)
    print("Source:", source)
    print("=" * 70)

    print("Raw HTML Length:", len(raw_html))
    print("Extracted Length:", len(article_content))
    print("Cleaned Length:", len(cleaned_article))

    print("\nArticle Beginning:")
    print(cleaned_article[:1000])

    print("\nArticle Ending:")
    print(cleaned_article[-1000:])
