# 📄 AI Research Paper Reviewer & Summarizer

An AI-powered research assistance platform that helps students, researchers, and academics understand research papers faster.

The application allows users to upload research papers in PDF format, extract their content, identify important sections, generate AI-powered summaries, and produce a structured research review.

---

## 🚀 Features

- 📑 Upload research papers in PDF format
- 🔍 Extract text from research papers
- 🧩 Automatically detect major research-paper sections
- 🤖 Generate AI-powered section summaries
- 📝 Generate structured AI-assisted research reviews
- 🎯 Identify research objectives
- 💡 Analyze key research contributions
- 🔬 Analyze methodology and experimental evaluation
- 💪 Identify strengths of the research
- ⚠️ Identify limitations
- 🔁 Analyze reproducibility considerations
- 📊 Provide an overall assessment
- 🌐 Interactive Streamlit web interface
- 🔐 Secure API-key management using environment variables
- 📚 Semantic Scholar integration for research-paper discovery
- 🧪 Automated testing for core components

---

## 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │        User          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Streamlit Web App    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     PDF Upload       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   PDF Text Extractor │
                         │      (PyMuPDF)       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Section Parser     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    AI Analysis       │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    ▼               ▼                ▼
             ┌─────────────┐ ┌─────────────┐ ┌──────────────┐
             │   Summary   │ │    Review   │ │ Future Gaps  │
             └─────────────┘ └─────────────┘ └──────────────┘
                    │               │                │
                    └───────────────┼────────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │   Research Insights  │
                         └──────────────────────┘
'''
## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Web application and user interface |
| OpenAI API | AI-powered summarization and paper review |
| Semantic Scholar API | Research-paper search and metadata |
| PyMuPDF | PDF text extraction |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine-learning utilities |
| NLTK | Natural language processing |
| Pydantic | Data validation |
| Requests | API communication |
| python-dotenv | Environment variable management |
| Git | Version control |
| GitHub | Source-code hosting |

---

## 📁 Project Structure

```text
AI-Research-Paper-Reviewer/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── config/
│   └── settings.py
│
├── models/
│   └── __init__.py
│
├── services/
│   ├── __init__.py
│   ├── pdf_extractor.py
│   ├── reviewer.py
│   ├── section_parser.py
│   ├── semantic_scholar.py
│   └── summarizer.py
│
├── tests/
│   ├── __init__.py
│   └── test_section_parser.py
│
├── ui/
│   └── __init__.py
│
└── utils/
    └── __init__.py
