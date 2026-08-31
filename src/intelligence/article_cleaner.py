class ArticleCleaner:
    def clean(self, text: str) -> str:
        cleaned_text = text.strip()
        lines = cleaned_text.splitlines()
        cleaned_lines = []

        for line in lines:
            clean_line = line.strip()
            clean_line = " ".join(clean_line.split())

            if clean_line != "":
                cleaned_lines.append(clean_line)

        clean_content = "\n".join(cleaned_lines)
        return clean_content
