from src.intelligence.models import ArticleIntelligence


intelligence = ArticleIntelligence(
    summary="This article discusses a new AI model update.",
    key_points=[
        "The model improves reasoning.",
        "The model improves coding performance."
    ],
    why_it_matters="The development may improve complex AI tasks."
)


assert intelligence.summary == (
    "This article discusses a new AI model update."
)

assert len(intelligence.key_points) == 2

assert intelligence.why_it_matters == (
    "The development may improve complex AI tasks."
)

print("ArticleIntelligence model test passed.")