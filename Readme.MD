# Mini RAG using LangChain + PGVector + Streamlit

A Retrieval-Augmented Generation (RAG) application built using **LangChain**, **Google Gemini**, **PostgreSQL + PGVector**, and **Streamlit**.

The application allows users to upload PDF and TXT documents, index them into a PGVector database, and ask natural language questions based on the uploaded knowledge base.

The project also includes an evaluation pipeline using **RAGAS** to measure the quality of retrieval and generated responses.

---

## Features

- Upload PDF and TXT documents
- Multiple document support
- Semantic search using PGVector
- Ask questions through a Streamlit UI
- Rebuild the vector index whenever new documents are added
- Shows which uploaded documents were used to generate the answer
- Automated RAG evaluation using RAGAS
- Generates evaluation reports in CSV and JSON format

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini
- PostgreSQL + PGVector
- Docker
- RAGAS

---

## Project Structure

```text
mini-rag/
│
├── Data/
│
├── Uploads/
│
├── evaluation/
│   ├── dataset.py
│   ├── run_eval.py
│   └── results/
│       ├── report.csv
│       ├── report.json
│       └── summary.json
│
├── src/
│   ├── config.py
│   ├── embeddings.py
│   ├── ingest.py
│   ├── llm.py
│   ├── query.py
│   ├── utils.py
│   └── vector_store.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the PGVector container

```bash
docker run --name pgvector-container ^
-e POSTGRES_USER=langchain ^
-e POSTGRES_PASSWORD=langchain ^
-e POSTGRES_DB=langchain ^
-p 6024:5432 ^
-d pgvector/pgvector:pg16
```

### 4. Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY

DATABASE_URL=postgresql+psycopg://langchain:langchain@localhost:6024/langchain
```

---

## Running the Project

Start the Streamlit app

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Running the Evaluation

Run the RAGAS evaluation pipeline using:

```bash
python -m evaluation.run_eval
```

The evaluation generates the following reports:

- `evaluation/results/report.csv`
- `evaluation/results/report.json`
- `evaluation/results/summary.json`

The following RAGAS metrics are evaluated:

- Faithfulness
- Answer Relevancy
- Context Precision
- Context Recall