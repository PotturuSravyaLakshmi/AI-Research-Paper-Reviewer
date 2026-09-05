from typing import Dict

from openai import OpenAI

from config.settings import OPENAI_API_KEY, OPENAI_MODEL


class PaperSummarizer:
    """Generate AI-powered summaries from research paper sections."""

    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not configured.")

        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = OPENAI_MODEL

    def summarize_section(self, section_name: str, content: str) -> str:
        """Generate a concise summary for one research-paper section."""

        if not content or not content.strip():
            return "No content available."

        prompt = f"""
You are an academic research assistant.

Summarize the following section from a research paper.

Section: {section_name}

Requirements:
- Preserve the original meaning.
- Do not invent information.
- Keep important technical terms.
- Focus on the main ideas, methods, findings, and conclusions.
- Write in clear academic language.
- Keep the summary concise.

Research paper section:
{content}
"""

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text.strip()

    def summarize_sections(self, sections: Dict[str, str]) -> Dict[str, str]:
        """Generate AI summaries for all available sections."""

        summaries = {}

        for section_name, content in sections.items():
            summaries[section_name] = self.summarize_section(
                section_name,
                content,
            )

        return summaries