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
             │   Summary   │ │    Review   │ │   Insights   │
             └─────────────┘ └─────────────┘ └──────────────┘
                    │               │                │
                    └───────────────┼────────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │   Research Insights  │
                         └──────────────────────┘
```

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
```
# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/PotturuSravyaLakshmi/AI-Research-Paper-Reviewer.git
```

Move into the project directory:

```bash
cd AI-Research-Paper-Reviewer
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

### Linux / macOS

```bash
python3 -m venv .venv
```

---

## 3. Activate the Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Configuration

This project uses API keys for AI analysis and research-paper services.

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
SEMANTIC_SCHOLAR_API_KEY=your_semantic_scholar_api_key
```

You can use `.env.example` as a template.

### Important Security Note

**Never upload your `.env` file to GitHub.**

API keys should always be stored as environment variables.

The project's `.gitignore` file prevents `.env` from being committed.

---

# ▶️ Running the Application

After activating the virtual environment, run:

```bash
streamlit run app.py
```

Streamlit will provide a local URL, normally:

```text
http://localhost:8501
```

Open the URL in your web browser.

---

# 📑 How to Use

### Step 1

Launch the application.

### Step 2

Upload a research paper in PDF format.

### Step 3

Click:

```text
Analyze Research Paper
```

### Step 4

The application extracts the text from the PDF.

### Step 5

The section parser identifies important sections such as:

- Abstract
- Introduction
- Background
- Model Architecture
- Training
- Results
- Conclusion
- References

### Step 6

The AI summarization module generates concise summaries.

### Step 7

The AI review module generates a structured analysis containing:

1. Research Objective
2. Key Contribution
3. Methodology
4. Experimental Evaluation
5. Strengths
6. Limitations
7. Reproducibility Considerations
8. Overall Assessment

---

# 🤖 AI-Assisted Analysis

The project uses Generative AI to assist with research-paper understanding.

The AI analysis is designed to:

- Preserve the meaning of the source material
- Focus on information available in the paper
- Avoid intentionally inventing unsupported information
- Highlight important technical concepts
- Provide structured research insights
- Help users understand papers more efficiently

---

# 🔬 Research Paper Processing Pipeline

```text
PDF
 │
 ▼
Text Extraction
 │
 ▼
Text Cleaning
 │
 ▼
Section Detection
 │
 ▼
Section-wise Analysis
 │
 ├───────────────┐
 ▼               ▼
AI Summary    AI Review
 │               │
 └───────┬───────┘
         ▼
 Research Insights
```

---

# 🧪 Testing

The project contains tests for core components.

Run the test suite using:

```bash
python -m pytest
```

If `pytest` is not installed:

```bash
pip install pytest
```

Then run:

```bash
python -m pytest
```

---

# 🔐 Responsible AI

This project is designed as an **AI-assisted research-support tool**.

The generated summaries and reviews should always be verified against the original research paper.

The system is **not intended to replace**:

- Human researchers
- Academic experts
- Peer reviewers
- Independent scientific judgment

Users should consult the original paper before making academic or research decisions based on AI-generated output.

---

# 📌 Example Research Paper

The project can be tested using publicly available research papers.

One example is:

**Attention Is All You Need**

Vaswani et al.

The paper introduced the Transformer architecture and is commonly used as an example for research-paper analysis.

---

# 🔮 Future Enhancements

The project is designed to support additional research-assistance capabilities.

Planned improvements include:

- 🔎 Automated research-gap detection
- 📚 Multi-paper comparison
- 🔗 Citation and reference analysis
- 📊 Paper comparison dashboard
- 📈 Citation analysis and visualization
- 📥 Export reports to PDF
- 📄 Export analysis to JSON
- 📊 Export results to CSV
- 🔍 Improved research-paper search
- 🧠 Advanced NLP-based analysis
- 🎨 Professional dashboard and visualizations
- ☁️ Cloud deployment
- 🧪 Expanded automated testing
- 📱 Improved responsive interface

---

# 🎯 Project Objectives

The main objectives of this project are:

1. Reduce the time required to understand research papers.
2. Automatically extract useful information from PDF documents.
3. Generate concise and meaningful summaries.
4. Provide structured AI-assisted research reviews.
5. Help students and researchers identify important research insights.
6. Create an easy-to-use web-based research assistance platform.
7. Demonstrate the practical application of Generative AI, NLP, and Python.

---

# 💡 Key Learning Outcomes

Through this project, the following technologies and concepts are demonstrated:

- Python application development
- REST API integration
- Generative AI
- Natural Language Processing
- PDF processing
- Text extraction
- Text preprocessing
- Prompt engineering
- Streamlit application development
- Environment-variable management
- Software modularization
- Unit testing
- Git and GitHub
- API error handling

---

# 👩‍💻 Author

## Potturu Venkata Siva Naga Sravya Lakshmi

**B.Tech – Computer Science & Engineering**

Interested in:

- Python
- Data Analytics
- Artificial Intelligence
- Machine Learning
- Generative AI
- Natural Language Processing
- Software Development

---

# ⭐ Project Goal

The goal of this project is to build a practical AI-powered research assistant that combines **PDF processing, NLP, research-paper metadata, and Generative AI** into a single platform.

The system aims to make research-paper analysis faster, more structured, and easier to understand while keeping the original research paper as the primary source of information.
