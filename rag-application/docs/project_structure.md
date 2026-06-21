# RAG Application Project Structure

This document outlines the recommended directory structure for a Python-based Retrieval-Augmented Generation (RAG) application using LangChain, Chroma DB, and Gemini/Groq LLMs.

## Directory Layout

```text
d:\ai-projects\
└── rag-application/       # The RAG project directory
    ├── data/              # Raw document files to be ingested (PDFs, markdown, texts, etc.)
    ├── db/                # Local vector database storage (Chroma database files)
    ├── docs/              # Project documentation (packages, structure guides)
    │   ├── packages.md
    │   └── project_structure.md
    ├── src/               # Source code of the RAG application
    │   ├── __init__.py
    │   ├── config.py      # Configuration and environment variables management
    │   ├── ingest.py      # Document loader, text splitter, and vector indexing logic
    │   ├── retrieval.py   # Query expansion, similarity search, and retrieval pipelines
    │   ├── generation.py  # Prompt templates and LLM response generation logic
    │   └── main.py        # Application entry point / main orchestration workflow
    ├── .env.template      # Sample environment file template (API keys, DB paths)
    └── requirements.txt   # Project python package dependencies
```

---

## Detailed Component Explanations

### 1. `rag-application/data/`
Place your source documents (e.g., policy manuals, research papers, custom datasets) here. Document loaders in `rag-application/src/ingest.py` will read from this directory.

### 2. `rag-application/db/`
This folder holds the persistent sqlite database files created by **Chroma DB**. Keeping it in a separate folder makes it easy to delete or re-index without affecting code. *(Note: This folder is excluded from Git tracking in the root `.gitignore`)*.

### 3. `rag-application/src/config.py`
Manages system configuration using `pydantic` or `python-dotenv`. It loads API keys (e.g., `GEMINI_API_KEY`, `GROQ_API_KEY`) and global settings like embedding model names, chunk sizes, and overlap parameters.

### 4. `rag-application/src/ingest.py`
Handles the data ingestion pipeline:
*   **Loading**: Reads files from the `rag-application/data/` directory using libraries like `pypdf` or `beautifulsoup4`.
*   **Splitting**: Breaks documents down into manageable, semantic chunks (using LangChain's `RecursiveCharacterTextSplitter`).
*   **Embedding & Storing**: Uses embedding models to vectorize the chunks and writes them into Chroma DB in the `rag-application/db/` folder.

### 5. `rag-application/src/retrieval.py`
Responsible for finding relevant chunks matching the user's query:
*   Initializes the Chroma DB vector store connection.
*   Converts the query into vector embeddings.
*   Performs similarity search to retrieve top-$k$ relevant chunks.
*   *(Optional)*: Implements re-ranking (e.g., Cohere) or query expansion.

### 6. `rag-application/src/generation.py`
Sets up prompt templates and interfaces with LLMs:
*   Formats the retrieved contexts and user query into a structured system prompt.
*   Sends the prompt to Gemini or Groq LLMs.
*   Formats and returns the generated answer.

### 7. `rag-application/src/main.py`
The orchestration layer. It exposes a simple command-line interface (CLI) or function to accept questions, trigger the retrieval from `retrieval.py`, feed the results to `generation.py`, and display the answer to the user.

