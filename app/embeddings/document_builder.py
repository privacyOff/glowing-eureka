class SearchDocumentBuilder:

    @staticmethod
    def build(call) -> str:

        parts = []

        if call.categories:

            category_names = [
                c.category
                for c in call.categories
            ]

            parts.append(
                f"Categories: {', '.join(category_names)}"
            )

        if call.summary:

            parts.append(
                f"Summary:\n{call.summary}"
            )

        parts.append(
            f"Transcript:\n{call.transcript}"
        )

        return "\n\n".join(parts)