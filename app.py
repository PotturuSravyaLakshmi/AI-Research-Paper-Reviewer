import streamlit as st

from services.pdf_extractor import PDFExtractor
from services.section_parser import SectionParser
from services.summarizer import PaperSummarizer
from services.reviewer import PaperReviewer


st.set_page_config(
    page_title="AI Research Paper Reviewer",
    page_icon="📄",
    layout="wide",
)


st.title("📄 AI Research Paper Reviewer")
st.write(
    "Upload a research paper and use AI to extract, summarize, "
    "and review its content."
)

st.divider()


uploaded_file = st.file_uploader(
    "Upload a research paper PDF",
    type=["pdf"],
)


if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("🔍 Analyze Research Paper"):

        with st.spinner("Extracting text from the paper..."):

            pdf_path = "data/pdfs/uploaded_paper.pdf"

            with open(pdf_path, "wb") as file:
                file.write(uploaded_file.getbuffer())

            extractor = PDFExtractor()
            text = extractor.extract_text(pdf_path)

        st.success("PDF text extracted successfully!")

        with st.spinner("Detecting research paper sections..."):

            parser = SectionParser()
            sections = parser.parse_sections(text)

        st.success(f"Detected {len(sections)} sections.")

        st.subheader("📑 Detected Sections")

        for section in sections:
            st.write(f"• {section.title()}")

        st.divider()

        with st.spinner("Generating AI summary..."):

            summarizer = PaperSummarizer()

            abstract = sections.get("abstract", "")

            if abstract:
                summary = summarizer.summarize_section(
                    "abstract",
                    abstract,
                )
            else:
                summary = "Abstract section was not detected."

        st.subheader("📝 AI Summary")
        st.write(summary)

        st.divider()

        with st.spinner("Generating AI research review..."):

            reviewer = PaperReviewer()
            review = reviewer.review_paper(sections)

        st.subheader("🤖 AI Research Review")
        st.markdown(review)