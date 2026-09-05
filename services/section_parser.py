import re


class SectionParser:
    """Identify and organize common sections in research papers."""

    SECTION_NAMES = {
        "abstract",
        "introduction",
        "background",
        "related work",
        "literature review",
        "model architecture",
        "methodology",
        "methods",
        "materials and methods",
        "approach",
        "training",
        "experiments",
        "experimental setup",
        "experimental results",
        "results",
        "discussion",
        "results and discussion",
        "analysis",
        "evaluation",
        "conclusion",
        "future work",
        "limitations",
        "acknowledgements",
        "references",
    }

    def _normalize_heading(self, line: str) -> str:
        """Normalize a possible section heading."""

        heading = line.strip()

        # Remove numbered headings:
        # 1 Introduction
        # 2. Methodology
        # 3.1 Experiments
        # IV. Results
        heading = re.sub(
            r"^(?:\d+(?:\.\d+)*|[IVXLCDM]+)[\s.)-]+",
            "",
            heading,
            flags=re.IGNORECASE,
        )

        # Remove trailing punctuation
        heading = re.sub(r"[:\-]+$", "", heading)

        return heading.strip().lower()

    def _is_section_heading(self, line: str) -> bool:
        """Check whether a line is a recognized section heading."""

        if not line.strip():
            return False

        normalized = self._normalize_heading(line)

        # Exact match
        if normalized in self.SECTION_NAMES:
            return True

        # Handle uppercase headings
        if line.strip().isupper():
            return normalized in self.SECTION_NAMES

        return False

    def parse_sections(self, text: str) -> dict:
        """
        Split research-paper text into recognized sections.

        Args:
            text: Extracted PDF text.

        Returns:
            Dictionary containing section names and their text.
        """

        if not text or not text.strip():
            raise ValueError("No text was provided for section parsing.")

        lines = text.splitlines()

        sections = {}
        current_section = None
        current_content = []

        for line in lines:
            cleaned_line = line.strip()

            if not cleaned_line:
                continue

            if self._is_section_heading(cleaned_line):

                # Save previous section
                if current_section and current_content:
                    sections[current_section] = "\n".join(
                        current_content
                    ).strip()

                current_section = self._normalize_heading(cleaned_line)
                current_content = []

            else:
                current_content.append(cleaned_line)

        # Save final section
        if current_section and current_content:
            sections[current_section] = "\n".join(
                current_content
            ).strip()

        return sections