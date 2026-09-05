from typing import Dict

from openai import OpenAI

from config.settings import OPENAI_API_KEY, OPENAI_MODEL


class PaperReviewer:
    """Perform AI-assisted structured review of research papers."""

    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not configured.")

        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL

    def review_paper(self, sections: Dict[str, str]) -> str:
        """Generate a structured review from research paper sections."""

        selected_sections = []

        for section_name in [
            "abstract",
            "introduction",
            "background",
            "model architecture",
            "methodology",
            "training",
            "results",
            "discussion",
            "conclusion",
        ]:
            if section_name in sections:
                selected_sections.append(
                    f"## {section_name.title()}\n{sections[section_name]}"
                )

        paper_text = "\n\n".join(selected_sections)

        prompt = f"""
You are an academic research assistant helping review a research paper.

Analyze the provided paper content and produce a structured,
evidence-based review.

Do not invent information that is not present in the paper.

Use the following structure:

1. Research Objective
2. Key Contribution
3. Methodology
4. Experimental Evaluation
5. Strengths
6. Limitations
7. Reproducibility Considerations
8. Overall Assessment

For each point, explain your reasoning using information from the
provided paper.

Paper content:

{paper_text}
"""

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text.strip()