from bs4 import BeautifulSoup


class ArticleExtractor:

    def extract(self, raw_html: str, source: str) -> str:
        soup = BeautifulSoup(raw_html, "html.parser")

        # Select the main article container for each source
        if source == "OpenAI":
            article_container = soup.find("article")

        elif source == "Anthropic":
            article_container = soup.find("main")

        elif source == "DeepMind":
            article_container = soup.find("main")

        else:
            raise ValueError("Source not found")

        # Make sure article content was found
        if article_container is None:
            raise ValueError("Article content not found")

        # -------------------------
        # DeepMind-specific cleanup
        # -------------------------
        if source == "DeepMind":
            headings = article_container.find_all("h2")

            for heading in headings:
                text = heading.get_text(
                    separator="\n",
                    strip=True
                )

                if text == "Related posts":
                    related_section = heading.find_parent("section")

                    if related_section is not None:
                        related_section.decompose()

            share_section = article_container.find(
                "div",
                class_="cover__button-group"
            )

            if share_section is not None:
                share_section.decompose()

            copy_button = article_container.find(
                "button",
                class_="share-list__item--copy"
            )

            if copy_button is not None:
                copy_button.decompose()

        # -------------------------
        # OpenAI-specific cleanup
        # -------------------------
        if source == "OpenAI":

            # Remove table of contents
            toc_button = article_container.find(
                "button",
                class_="h-toc-button-h"
            )

            if toc_button is not None:
                toc_parent = toc_button.find_parent("div")

                if toc_parent is not None:
                    toc_parent.decompose()

            # Remove Share / Loading component
            share_candidates = article_container.find_all(
                "div",
                attrs={"aria-haspopup": "dialog"}
            )

            for candidate in share_candidates:
                text = candidate.get_text(
                    separator="\n",
                    strip=True
                )

                if text == "Share":
                    parent_1 = candidate.parent

                    if parent_1 is not None:
                        parent_2 = parent_1.parent

                        if parent_2 is not None:
                            parent_3 = parent_2.parent

                            if parent_3 is not None:
                                parent_3.decompose()
                                break

            # Remove recommended articles section
            keep_reading_heading = article_container.find(
                "h2",
                string="Keep reading"
            )

            if keep_reading_heading is not None:
                heading_container = keep_reading_heading.parent

                if heading_container is not None:
                    recommendations_header = heading_container.parent

                    if recommendations_header is not None:
                        recommendations_wrapper = (
                            recommendations_header.parent
                        )

                        if recommendations_wrapper is not None:
                            recommendations_wrapper.decompose()

        # -------------------------
        # Anthropic-specific cleanup
        # -------------------------
        if source == "Anthropic":

            # Remove related content section
            related_heading = article_container.find(
                "h2",
                string="Related content"
            )

            if related_heading is not None:
                related_intro = related_heading.parent

                if related_intro is not None:
                    related_wrapper = related_intro.parent

                    if related_wrapper is not None:
                        related_wrapper.decompose()

            # Remove newsletter section
            newsletter_heading = article_container.find(
                "h2",
                string="Subscribe to Anthropic Science"
            )

            if newsletter_heading is not None:
                newsletter_text = newsletter_heading.parent

                if newsletter_text is not None:
                    newsletter_wrapper = newsletter_text.parent

                    if newsletter_wrapper is not None:
                        newsletter_wrapper.decompose()

        # -------------------------
        # Common cleanup
        # -------------------------
        elements = article_container.find_all(
            ["script", "style"]
        )

        for element in elements:
            element.decompose()

        # Convert remaining HTML into plain text
        article_text = article_container.get_text(
            separator="\n",
            strip=True
        )
        return article_text
