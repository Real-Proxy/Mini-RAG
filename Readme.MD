# Mini RAG using LangChain + PGVector

This is a simple Retrieval-Augmented Generation (RAG) project that I built to understand the basics of document ingestion, embeddings, vector databases, and semantic search using LangChain and PGVector.

The project uses a sample employee handbook as the knowledge base. A user's question is converted into an embedding, relevant document chunks are retrieved from PGVector, and the retrieved context is sent to Gemini to generate the final answer.

---

## Tech Stack

- Python
- LangChain
- Google Gemini
- PostgreSQL + PGVector
- Docker

---

## Project Structure

```
mini-rag/
│
├── Data/
│   └── employee_handbook.txt
│
├── src/
│   ├── config.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── llm.py
│   ├── ingest.py
│   ├── query.py
│   └── main.py
│
├── requirements.txt
├── .env
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

### 4. Add a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY

DATABASE_URL=postgresql+psycopg://langchain:langchain@localhost:6024/langchain
```

---

## Running the Project

First ingest the document into PGVector.

```bash
python src/ingest.py
```

Then start the application.

```bash
python src/main.py
```

---

## Sample

```
Ask a question:

> Where is HR located?

Answer:

The HR department is located on the third floor.
```

