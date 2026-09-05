from pathlib import Path

import fitz


class PDFExtractor:
    """Extract text from research paper PDF files."""

    def extract_text(self, pdf_path: str) -> str:
        """
        Extract text from all pages of a PDF.

        Args:
            pdf_path: Path to the PDF file.

        Returns:
            Extracted text as a single string.
        """

        path = Path(pdf_path)

        if not path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        if path.suffix.lower() != ".pdf":
            raise ValueError("The provided file is not a PDF.")

        extracted_pages = []

        try:
            with fitz.open(path) as document:
                for page in document:
                    text = page.get_text("text")

                    if text.strip():
                        extracted_pages.append(text)

        except Exception as error:
            raise RuntimeError(
                f"Failed to extract text from PDF: {error}"
            ) from error

        extracted_text = "\n".join(extracted_pages).strip()

        if not extracted_text:
            raise ValueError(
                "No readable text was found in the PDF. "
                "The file may contain scanned images instead of text."
            )

        return extracted_text