# AI_Github_Engineering_Assistant

An AI-powered GitHub repository analysis system that can clone repositories, index source code, and answer technical questions about the codebase using Retrieval-Augmented Generation (RAG).

The project combines:
- FastAPI backend
- Streamlit frontend
- OpenAI embeddings
- FAISS vector search
- GitHub repository parsing
- RAG pipeline for code understanding

---

# Features

- Clone GitHub repositories dynamically
- Parse source code files
- Chunk and embed repository content
- Store embeddings using FAISS
- Ask questions about the repository
- AI-generated answers using GPT models
- Streamlit frontend UI
- FastAPI backend API

---

# Tech Stack

## Backend
- Python
- FastAPI
- Uvicorn

## AI / RAG
- OpenAI API
- Embeddings
- FAISS
- LangChain
- Retrieval-Augmented Generation (RAG)

## Frontend
- Streamlit

---

# Project Structure

```text
AI_Github_Engineering_Assistant/
│
├── agent.py
├── app.py
├── frontend.py
├── rag.py
├── repo_tools.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshot/
│   └── Screenshot 2026-05-08 at 16.51.46.png
│
└── repos/
```

---

# Screenshot

![Application UI](screenshot/Screenshot%202026-05-08%20at%2016.51.46.png)

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Github_Engineering_Assistant.git
cd AI_Github_Engineering_Assistant
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Setup OpenAI API Key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# Run Backend

```bash
uvicorn app:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Run Frontend

Open a new terminal:

```bash
source venv/bin/activate
streamlit run frontend.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# How It Works

```text
GitHub Repository URL
        ↓
Clone Repository
        ↓
Read Source Code Files
        ↓
Chunk Repository Content
        ↓
Generate Embeddings
        ↓
Store in FAISS
        ↓
Retrieve Relevant Chunks
        ↓
LLM Generates Answer
```

---

# Example Questions

- What technologies are used in this repository?
- Explain the project architecture
- How does authentication work?
- Which APIs are implemented?
- Summarize the backend workflow
- Explain the database layer

---

# Future Improvements

- Multi-repository support
- Persistent vector database
- Docker deployment
- GitHub OAuth
- Code summarization agents
- Multi-agent architecture
- Kubernetes deployment
- CI/CD integration

---

# Resume Description

Built an AI-powered GitHub Engineering Assistant using FastAPI, Streamlit, OpenAI embeddings, and FAISS to analyze repositories and answer technical questions using Retrieval-Augmented Generation (RAG).
