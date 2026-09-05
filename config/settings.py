import os
from pathlib import Path

from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env
load_dotenv(BASE_DIR / ".env")


# Semantic Scholar API
SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-5.6-luna"
# API configuration
SEMANTIC_SCHOLAR_BASE_URL = "https://api.semanticscholar.org/graph/v1"
REQUEST_TIMEOUT = 30
SEARCH_LIMIT = 10


# Project data directories
DATA_DIR = BASE_DIR / "data"
PDF_DIR = DATA_DIR / "pdfs"
METADATA_DIR = DATA_DIR / "metadata"
OUTPUT_DIR = DATA_DIR / "outputs"


# Create directories if they don't exist
PDF_DIR.mkdir(parents=True, exist_ok=True)
METADATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)