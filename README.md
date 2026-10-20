# DocuMind AI

A Streamlit document Q&A workspace that extracts text from a PDF, retrieves relevant passages using TF-IDF similarity, and optionally generates grounded answers using a local Ollama model.

## Features
- PDF upload and text extraction
- Text chunking with page numbers
- TF-IDF retrieval of relevant passages
- Source page citations
- Optional local AI generation through Ollama
- Responsive, readable dashboard UI

## Run on Windows
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Optional local AI
Install Ollama from https://ollama.com/download and run:
```powershell
ollama pull qwen2.5:3b
```
Keep Ollama running. Without it, the app still retrieves relevant excerpts but does not synthesize answers.

## Limitations
- Scanned PDFs need OCR, not included.
- Retrieval uses TF-IDF, not embeddings.
- The app handles one PDF at a time in this starter version.

## Test checklist
- [ ] Upload a text-based PDF
- [ ] Process it and confirm chunks are indexed
- [ ] Ask a question answerable from the PDF
- [ ] Confirm source page numbers appear
- [ ] Test without Ollama and confirm relevant excerpts still appear
