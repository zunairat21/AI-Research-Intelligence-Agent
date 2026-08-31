from src.intelligence.article_extractor import ArticleExtractor

extractor = ArticleExtractor()
raw_html = """
<html>
    <body>
        <main>
            <div>
                <h1>AI Research Article</h1>
                <p>This is meaningful article evidence.</p>
            </div>

            <div class="page-wrapper">
                <div>
                    <h2>Related content</h2>
                </div>
                <div>
                    <p>Recommended article</p>
                    <p>Read more</p>
                </div>
            </div>

            <div class="newsletter-wrapper">
                <div>
                    <h2>Subscribe to Anthropic Science</h2>
                    <p>Newsletter description.</p>
                </div>
                <div>
                    <form>Subscribe form</form>
                </div>
            </div>

            <script>console.log("noise")</script>
            <style>body { font-size: 12px; }</style>
        </main>
    </body>
</html>
"""

article_content = extractor.extract(
    raw_html,
    "Anthropic"
)
print("Extracted content:")
print(article_content)

print(
    "\nArticle content preserved:",
    "This is meaningful article evidence." in article_content
)

print(
    "Related content removed:",
    "Related content" not in article_content
)

print(
    "Newsletter removed:",
    "Subscribe to Anthropic Science" not in article_content
)

print(
    "Script removed:",
    'console.log("noise")' not in article_content
)
