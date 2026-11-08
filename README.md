#  DocuMind AI — Intelligent Document Q&A Workspace

<p align="center">
  <strong>Ask Questions. Discover Insights. Understand Your Documents.</strong>
  <br/>
  A document intelligence application that transforms PDF files into searchable knowledge using text extraction, TF-IDF retrieval and optional local AI-powered answer generation.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Ollama-Local%20AI-black?style=for-the-badge&logo=ollama&logoColor=white" />
  <img src="https://img.shields.io/badge/TF--IDF-Text%20Retrieval-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active%20Development-success?style=for-the-badge" />
</p>

---

##  Overview

**DocuMind AI** is a Python-based document question-answering workspace designed to make information inside PDF documents easier to access and understand.

Instead of manually searching through lengthy documents, users can upload a PDF, process its contents, and ask questions using a conversational interface.

The application extracts document text, divides it into smaller chunks, retrieves relevant passages using TF-IDF similarity, and displays supporting source-page references.

For enhanced question answering, DocuMind AI optionally integrates with a locally running Ollama model to generate answers grounded in retrieved document content.

The application can also operate without Ollama, providing relevant retrieved excerpts directly.

##  Key Features

| Feature | Description |
|---|---|
|  PDF Upload | Upload text-based PDF documents |
|  Text Extraction | Extract readable content from PDF pages |
|  Text Chunking | Divide documents into smaller searchable passages |
|  TF-IDF Retrieval | Retrieve relevant passages based on query similarity |
|  Source Citations | Display page references for retrieved information |
|  Local AI Integration | Generate grounded answers using Ollama |
|  Document Q&A | Ask questions about uploaded documents |
|  Flexible Operation | Use retrieval without requiring a local AI model |
|  Responsive Dashboard | Access document analysis through a readable Streamlit interface |

##  Technology Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Streamlit |
| PDF Processing | PyMuPDF |
| Text Retrieval | scikit-learn |
| Retrieval Algorithm | TF-IDF + Cosine Similarity |
| Local AI Runtime | Ollama |
| Language Model | Qwen 2.5 3B |
| Frontend | Streamlit UI |

##  How DocuMind AI Works

```text
             Upload PDF
                 |
                 ▼
          PDF Text Extraction
                 |
                 ▼
           Text Processing
                 |
                 ▼
          Document Chunking
          + Page References
                 |
                 ▼
          TF-IDF Vectorization
                 |
                 ▼
           User Question
                 |
                 ▼
          Similarity Retrieval
                 |
                 ▼
         Relevant Text Chunks
                 |
           ┌─────┴─────┐
           ▼           ▼
      Show Relevant   Ollama
        Excerpts      (Optional)
           |           |
           |           ▼
           |      Grounded Answer
           |           |
           └─────┬─────┘
                 |
                 ▼
         Answer + Page Sources
```

##  Getting Started

Follow these instructions to run DocuMind AI locally on Windows.

### Prerequisites

- Python 3.10 or later
- pip
- Git
- Optional: Ollama for local AI-powered answer generation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project directory:

```bash
cd DocuMind-AI
```

### 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 3. Activate the Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Start the Application

```powershell
python -m streamlit run app.py
```

### 6. Open DocuMind AI

Visit:

**http://localhost:8501**

The document Q&A workspace will be available in your browser.

##  Optional Local AI Integration

DocuMind AI supports local answer generation through Ollama.

This allows users to generate answers using a locally running language model rather than depending on a hosted AI API.

### 1. Install Ollama

Download Ollama:

https://ollama.com/download

### 2. Download the Model

Open PowerShell and execute:

```powershell
ollama pull qwen2.5:3b
```

### 3. Keep Ollama Running

Make sure the Ollama service is running while using the application.

The application can then use the configured local model to generate answers from retrieved document passages.

**Without Ollama:** DocuMind AI continues to work as a document retrieval system, displaying relevant excerpts and their source pages without generating synthesized answers.

##  Retrieval Methodology

DocuMind AI uses a retrieval-based approach to locate information inside uploaded PDF documents.

**1. PDF Text Extraction**

Document text is extracted page by page using PyMuPDF.

**2. Text Chunking**

Extracted content is divided into smaller passages while retaining page references.

**3. TF-IDF Vectorization**

The document chunks are converted into numerical representations using Term Frequency–Inverse Document Frequency.

**4. Similarity Retrieval**

Cosine similarity is used to identify passages that are most relevant to the user's question.

**5. Grounded Answer Generation**

When Ollama is available, retrieved passages are supplied as context to the local language model to generate an answer.

**6. Source References**

Relevant page numbers are displayed alongside retrieved information to help users verify the answers against the original document.

##  Project Structure

```text
DocuMind-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── PDF extraction
│   ├── text processing
│   └── retrieval logic
│
└── static/
    └── application assets
```

*The structure above is a conceptual overview. Adjust the filenames and folders to match the actual repository implementation.*

##  Privacy & Data Handling

DocuMind AI supports local document processing and optional local AI inference.

- PDF documents are processed by the application.
- Ollama provides local model inference.
- No hosted AI API is required for the local Ollama workflow.
- Review temporary file handling and storage behaviour before deployment.
- Avoid uploading confidential documents to publicly accessible deployments without appropriate security controls.

##  Current Limitations

DocuMind AI is a document Q&A prototype with the following limitations:

- Scanned PDFs require OCR, which is not currently included.
- Retrieval uses TF-IDF rather than semantic embedding models.
- Only one PDF document is supported at a time in the current starter version.
- Retrieval quality depends on document text quality and chunking.
- Generated answers may contain inaccuracies and should be checked against the cited source pages.
- Local AI generation requires Ollama and a compatible model to be available.

##  Future Enhancements

Potential improvements for future versions:

- **OCR Integration:** Support scanned PDFs and image-based documents.
- **Semantic Search:** Introduce embedding-based retrieval for improved contextual matching.
- **Multi-Document Q&A:** Search across multiple uploaded documents.
- **Conversation History:** Preserve previous questions and answers.
- **Advanced Citations:** Display supporting passages alongside page references.
- **Document Summarization:** Generate structured summaries of lengthy documents.
- **Improved Retrieval:** Experiment with hybrid search and reranking.
- **Additional Local Models:** Support configurable Ollama models.

##  Project Objectives

- Simplify information retrieval from lengthy PDF documents.
- Explore natural language processing and information retrieval techniques.
- Implement TF-IDF-based document search.
- Integrate local language models for grounded question answering.
- Improve answer traceability through page-level citations.
- Demonstrate practical Python, Streamlit and AI application development skills.

##  License

Add a `LICENSE` file to specify the terms under which DocuMind AI can be used, modified and distributed.

---

<p align="center">
  <strong> DocuMind AI</strong>
  <br/>
  <em>Your Documents. Your Knowledge. One Conversation.</em>
  <br/><br/>
  Built with Python, Streamlit, scikit-learn and Ollama.
</p>
