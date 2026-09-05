import time
import requests

from config.settings import (
    SEMANTIC_SCHOLAR_API_KEY,
    SEMANTIC_SCHOLAR_BASE_URL,
    REQUEST_TIMEOUT,
    SEARCH_LIMIT,
)


class SemanticScholarService:
    """Service for interacting with the Semantic Scholar API."""

    def __init__(self):
        self.base_url = SEMANTIC_SCHOLAR_BASE_URL

        self.headers = {
            "User-Agent": "AI-Research-Paper-Reviewer/1.0"
        }

        if SEMANTIC_SCHOLAR_API_KEY:
            self.headers["x-api-key"] = SEMANTIC_SCHOLAR_API_KEY

    def search_papers(self, query: str, limit: int = SEARCH_LIMIT):
        """Search for research papers using Semantic Scholar."""

        url = f"{self.base_url}/paper/search"

        params = {
            "query": query,
            "limit": min(limit, 10),
            "fields": (
                "paperId,title,authors,year,abstract,url,"
                "isOpenAccess,openAccessPdf,externalIds,citationCount"
            ),
        }

        try:
            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=REQUEST_TIMEOUT,
            )

            if response.status_code == 429:
                print("Semantic Scholar rate limit reached. Please try again later.")
                return []

            if response.status_code == 403:
                print("Semantic Scholar access denied. Check your API key.")
                return []

            response.raise_for_status()

            data = response.json()
            return data.get("data", [])

        except requests.exceptions.Timeout:
            print("Semantic Scholar request timed out.")
            return []

        except requests.exceptions.RequestException as error:
            print(f"Semantic Scholar API error: {error}")
            return []