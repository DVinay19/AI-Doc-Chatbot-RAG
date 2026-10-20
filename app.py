
import html
import requests
import streamlit as st
from datetime import datetime
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- PROFESSIONAL STYLING --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

:root {
    --page:#f4f7fb;
    --surface:#ffffff;
    --navy:#172b4d;
    --text:#263750;
    --muted:#718096;
    --border:#e2eaf4;
    --blue:#2859a8;
    --teal:#128b91;
}

.stApp {
    background:radial-gradient(ellipse at 85% 0%,#e7f2f7,transparent 36%),var(--page);
    color:var(--text);
    font-family:'DM Sans',sans-serif;
}
.block-container {max-width:1440px;padding:1.6rem 2rem 5rem;}
[data-testid="stHeader"] {background:rgba(244,247,251,.94);}
h1,h2,h3 {font-family:'Manrope',sans-serif!important;color:var(--navy)!important;}
p {line-height:1.7;}

[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#172b4d,#12223c);
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stMarkdown {
    color:#edf4ff!important;
}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
    color:#afc0d8!important;
}
[data-testid="stSidebar"] input {
    background:#fff!important;color:#172b4d!important;
    border-radius:9px!important;
}
[data-testid="stSidebar"] [data-testid="stFileUploader"] {
    background:rgba(255,255,255,.05);
    border:1px solid rgba(255,255,255,.13);
    border-radius:12px;padding:10px;
}

.hero {
    background:linear-gradient(120deg,#193d70,#245c94 56%,#12878e);
    padding:30px 34px;border-radius:19px;margin-bottom:24px;
    box-shadow:0 12px 30px #1f4b7c20;
}
.hero h1 {color:white!important;font-size:2.1rem!important;margin:0 0 8px;}
.hero p {color:#e6f2ff!important;margin:0;}

.metric {
    background:#fff;border:1px solid var(--border);border-radius:15px;
    padding:20px;min-height:100px;
    box-shadow:0 7px 25px #1e3a5f09;
}
.metric-label {color:var(--muted);font-size:.72rem;font-weight:800;letter-spacing:.8px;}
.metric-value {color:var(--blue);font-size:1.45rem;font-weight:800;overflow-wrap:anywhere;}

.section-heading {
    font-family:'Manrope',sans-serif;font-size:1.45rem;font-weight:800;
    color:var(--navy);margin:24px 0 8px;
}
.stButton>button {
    border-radius:10px;font-weight:700;
    border:1px solid #d8e3f1;transition:all .18s ease;
}
.stButton>button[kind="primary"] {
    background:linear-gradient(110deg,#2859a8,#147f91);
    color:white!important;border:none;
}
.stButton>button:hover {border-color:var(--blue);}

[data-testid="stChatInput"]>div,
[data-testid="stChatInput"] form {
    background:#fff!important;border:1px solid #d6e1ef!important;
    border-radius:13px!important;box-shadow:0 6px 22px #1e3a5f0c;
}
[data-testid="stChatInput"] textarea {
    color:#172b4d!important;-webkit-text-fill-color:#172b4d!important;
    caret-color:#172b4d!important;background:#fff!important;opacity:1!important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color:#8290a5!important;-webkit-text-fill-color:#8290a5!important;opacity:1!important;
}
[data-testid="stChatInput"] button {background:#2859a8!important;color:white!important;}

[data-testid="stChatMessage"] {
    background:white!important;border:1px solid var(--border)!important;
    border-radius:14px!important;padding:15px!important;
}
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {
    color:var(--text)!important;line-height:1.75;
}
.source {
    background:#f7faff;border:1px solid #dce7f5;border-left:4px solid #128b91;
    border-radius:10px;padding:14px;margin:10px 0;
}
.source-title {color:#2859a8;font-size:.75rem;font-weight:800;margin-bottom:8px;}
.source-text {color:#34445d;font-size:.9rem;line-height:1.8;white-space:pre-wrap;overflow-wrap:anywhere;}
.status-card {
    background:rgba(255,255,255,.07);border:1px solid #ffffff20;
    border-radius:10px;padding:12px;margin:8px 0;
}
[data-testid="stAlert"] {border-radius:11px;}
[data-testid="stExpander"] {background:#fff;border:1px solid var(--border);border-radius:11px;}
[data-testid="stCaptionContainer"] p {color:var(--muted);font-size:.82rem;}

@media(max-width:768px) {
    .block-container {padding:1rem 1rem 4rem;}
    .hero {padding:22px;border-radius:14px;}
    .hero h1 {font-size:1.7rem!important;}
}

/* Improve suggested-question button contrast */
.stButton > button {
    background: #ffffff !important;
    color: #2859a8 !important;
    border: 1px solid #d7e3f2 !important;
    min-height: 42px;
}

.stButton > button:hover {
    background: #edf5ff !important;
    color: #173b70 !important;
    border-color: #2859a8 !important;
}

/* Keep primary action button prominent */
.stButton > button[kind="primary"] {
    background: linear-gradient(110deg, #2859a8, #147f91) !important;
    color: #ffffff !important;
}

/* Readable source expander */
[data-testid="stExpander"] {
    background: #ffffff !important;
    border: 1px solid #dce7f5 !important;
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span {
    color: #263750 !important;
}

/* Consistent dashboard spacing */
[data-testid="stHorizontalBlock"] {
    gap: 16px;
}

/* Professional animated download button */
.stDownloadButton > button {
    position: relative;
    overflow: hidden;
    width: 100%;
    min-height: 48px;
    border: 1px solid #16a34a !important;
    border-radius: 12px !important;
    background: linear-gradient(110deg, #15803d, #16a34a, #059669) !important;
    background-size: 200% 100% !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    letter-spacing: 0.2px;
    box-shadow: 0 5px 16px rgba(22, 163, 74, 0.20);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    animation: downloadGlow 4s ease-in-out infinite;
}

.stDownloadButton > button,
.stDownloadButton > button p,
.stDownloadButton > button span {
    color: #ffffff !important;
}

.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(22, 163, 74, 0.32);
    border-color: #15803d !important;
}

.stDownloadButton > button:active {
    transform: translateY(0);
}

/* Soft moving gradient */
@keyframes downloadGlow {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

/* Respect reduced-motion preferences */
@media (prefers-reduced-motion: reduce) {
    .stDownloadButton > button {
        animation: none;
        transition: none;
    }
}
</style>
""", unsafe_allow_html=True)

# -------------------- SESSION STATE --------------------
defaults = {
    "chunks": [],
    "doc_name": "",
    "page_count": 0,
    "questions_asked": 0,
    "history": [],
    "pending_question": "",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------- PDF PROCESSING --------------------
def split_text(text, page_number, chunk_size=220, overlap=40):
    words = text.split()
    chunks = []
    step = max(1, chunk_size - overlap)

    for start in range(0, len(words), step):
        part = " ".join(words[start:start + chunk_size])
        if part:
            chunks.append({"text": part, "page": page_number})
    return chunks


def process_pdf(file):
    reader = PdfReader(file)
    chunks = []
    readable_pages = 0

    for page_number, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if text:
            readable_pages += 1
            chunks.extend(split_text(text, page_number))

    return chunks, len(reader.pages), readable_pages


# -------------------- SEARCH --------------------
def retrieve(question, chunks, limit=4):
    if not chunks:
        return []

    corpus = [item["text"] for item in chunks]

    try:
        vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
        )
        matrix = vectorizer.fit_transform(corpus + [question])
        scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
    except ValueError:
        return []

    results = []
    for index in scores.argsort()[::-1]:
        if scores[index] <= 0:
            continue
        result = dict(chunks[int(index)])
        result["score"] = float(scores[index])
        results.append(result)
        if len(results) >= limit:
            break

    return results


# -------------------- OLLAMA --------------------
def ollama_status():
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        response.raise_for_status()
        return True, response.json().get("models", [])
    except requests.RequestException:
        return False, []


def ask_ollama(question, sources, model):
    context = "\n\n".join(
        f"[Page {item['page']}] {item['text']}"
        for item in sources
    )

    prompt = f"""
You are DocuMind AI, an assistant answering questions about a PDF.
Answer clearly and simply using only the document context.
Do not invent facts. Mention source page numbers where possible.
If the context lacks the answer, say so honestly.

DOCUMENT CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=180,
    )
    response.raise_for_status()
    return response.json().get("response", "").strip()


# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.markdown("## 📂 Document Center")
    st.write("Upload a PDF to get started.")

    uploaded_file = st.file_uploader("Choose PDF", type=["pdf"])
    model_name = st.text_input("Ollama model name", value="qwen2.5:3b")

    connected, installed_models = ollama_status()
    model_names = [m.get("name", "") for m in installed_models]

    if connected:
        st.markdown(
            '<div class="status-card">🟢 <b>Ollama connected</b><br>'
            '<small>Local AI service is responding.</small></div>',
            unsafe_allow_html=True,
        )
        if model_name.strip() in model_names:
            st.caption("✅ Selected model is installed.")
        else:
            st.caption("⚠️ Model name not found in installed model list.")
    else:
        st.markdown(
            '<div class="status-card">🔴 <b>Ollama offline</b><br>'
            '<small>Start Ollama to enable AI answers.</small></div>',
            unsafe_allow_html=True,
        )

    if st.button("Process document", type="primary", use_container_width=True):
        if uploaded_file is None:
            st.warning("Please choose a PDF first.")
        else:
            try:
                with st.spinner("Processing PDF..."):
                    chunks, pages, readable = process_pdf(uploaded_file)

                if not chunks:
                    st.error("No selectable text found. Scanned PDFs need OCR.")
                else:
                    st.session_state.chunks = chunks
                    st.session_state.doc_name = uploaded_file.name
                    st.session_state.page_count = pages
                    st.session_state.questions_asked = 0
                    st.session_state.history = []
                    st.success(f"Processed {uploaded_file.name} successfully.")

                    if readable < pages:
                        st.info(f"Text extracted from {readable} of {pages} pages.")
            except Exception as error:
                st.error(f"Could not process PDF: {error}")

    st.divider()
    st.markdown("### Workspace")

    if st.session_state.doc_name:
        st.success(f"Indexed: {st.session_state.doc_name}")
        st.caption(
            f"{st.session_state.page_count} pages · "
            f"{len(st.session_state.chunks)} text chunks"
        )
    else:
        st.caption("No document indexed yet.")

    if st.button("Clear workspace", use_container_width=True):
        st.session_state.chunks = []
        st.session_state.doc_name = ""
        st.session_state.page_count = 0
        st.session_state.questions_asked = 0
        st.session_state.history = []
        st.rerun()


# -------------------- HEADER --------------------
st.markdown("""
<div class="hero">
    <h1>📚 DocuMind AI</h1>
    <p>Your intelligent document workspace. Ask questions, understand complex topics,
    and trace answers back to their PDF sources.</p>
</div>
""", unsafe_allow_html=True)

name = st.session_state.doc_name or "No document"
if len(name) > 25:
    name = name[:22] + "..."

columns = st.columns(3)
metrics = [
    ("ACTIVE DOCUMENT", name),
    ("TEXT CHUNKS", len(st.session_state.chunks)),
    ("QUESTIONS ASKED", st.session_state.questions_asked),
]

for column, (label, value) in zip(columns, metrics):
    with column:
        st.markdown(
            f'<div class="metric"><div class="metric-label">{html.escape(label)}'
            f'</div><div class="metric-value">{html.escape(str(value))}</div></div>',
            unsafe_allow_html=True,
        )

st.markdown(
    '<div class="section-heading">💬 Ask your document</div>',
    unsafe_allow_html=True,
)
st.write("Use a suggested question or type your own below.")

# -------------------- SUGGESTED QUESTIONS --------------------
suggestions = [
    "Summarize this document",
    "What skills are mentioned?",
    "Explain my projects simply",
]

button_columns = st.columns(3)
for index, suggestion in enumerate(suggestions):
    with button_columns[index]:
        if st.button(suggestion, use_container_width=True):
            st.session_state.pending_question = suggestion
            st.rerun()

# -------------------- CHAT HISTORY --------------------
for item in st.session_state.history:
    with st.chat_message("user"):
        st.write(item["question"])

    with st.chat_message("assistant"):
        if item.get("answer"):
            st.markdown(item["answer"])
        else:
            st.warning(item.get("error", "Could not generate an answer."))

        if item.get("sources"):
            with st.expander("📄 View document sources"):
                for source in item["sources"]:
                    st.markdown(
                        f"""
                        <div class="source">
                            <div class="source-title">
                                SOURCE · PAGE {source['page']}
                                · RELEVANCE {source.get('score', 0):.2f}
                            </div>
                            <div class="source-text">{html.escape(source['text'])}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

# -------------------- DOWNLOAD REPORT --------------------
if st.session_state.history:
    report_lines = [
        "DOCUMIND AI - CHAT REPORT",
        f"Document: {st.session_state.doc_name}",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "=" * 55,
        "",
    ]

    for number, item in enumerate(st.session_state.history, start=1):
        report_lines.extend([
            f"QUESTION {number}:",
            item["question"],
            "",
            "ANSWER:",
            item.get("answer") or item.get("error", "No answer available."),
            "",
            "SOURCES:",
        ])

        for source in item.get("sources", []):
            report_lines.append(
                f"Page {source['page']}: {source['text']}"
            )

        report_lines.extend(["", "-" * 55, ""])

    report_text = "\n".join(report_lines)

    st.download_button(
        "⬇️ Download chat report (.txt)",
        data=report_text,
        file_name="DocuMind_AI_Chat_Report.txt",
        mime="text/plain",
        use_container_width=True,
    )

# -------------------- QUESTION HANDLING --------------------
typed_question = st.chat_input("Ask a question about your uploaded PDF...")
question = typed_question or st.session_state.pending_question

if question:
    st.session_state.pending_question = ""

    if not st.session_state.chunks:
        st.warning("Upload and process a PDF in the sidebar first.")
    else:
        st.session_state.questions_asked += 1
        sources = retrieve(question, st.session_state.chunks, limit=4)

        # Broad questions can use the first few document passages as context.
        if not sources:
            sources = st.session_state.chunks[:4]

        answer = ""
        error_message = ""

        with st.spinner("DocuMind AI is generating your answer..."):
            try:
                answer = ask_ollama(
                    question,
                    sources,
                    model_name.strip() or "qwen2.5:3b",
                )
                if not answer:
                    error_message = "Ollama returned an empty answer."
            except requests.exceptions.ConnectionError:
                error_message = "Cannot connect to Ollama. Check that it is running."
            except requests.exceptions.Timeout:
                error_message = "The AI took too long to respond. Please try again."
            except requests.exceptions.HTTPError as error:
                error_message = f"Ollama error: {error.response.text[:300]}"
            except requests.exceptions.RequestException as error:
                error_message = f"Could not generate an answer: {error}"

        st.session_state.history.append({
            "question": question,
            "answer": answer,
            "error": error_message,
            "sources": sources,
        })
        st.rerun()

# -------------------- FOOTER --------------------
st.divider()
st.caption(
    "DocuMind AI · Python · Streamlit · TF-IDF Search · Ollama Local AI"
)
