import os
from src.config import DATA_DIR, DB_DIR, CHUNK_SIZE, CHUNK_OVERLAP

def load_documents(directory_path):
    """
    Load files (PDFs, text files, HTML) from the specified directory.
    """
    print(f"Loading documents from {directory_path}...")
    # TODO: Use pypdf for PDFs, BeautifulSoup for html, etc.
    documents = []
    return documents

def split_documents(documents):
    """
    Split documents into smaller semantic chunks.
    """
    print(f"Splitting documents with chunk size={CHUNK_SIZE}...")
    # TODO: Implement RecursiveCharacterTextSplitter from langchain
    chunks = []
    return chunks

def index_chunks(chunks, db_path):
    """
    Vectorize chunks and save them into the Chroma vector database.
    """
    print(f"Indexing chunks in database at {db_path}...")
    # TODO: Initialize embeddings and Chroma DB, save documents
    pass

def run_ingestion():
    docs = load_documents(DATA_DIR)
    chunks = split_documents(docs)
    index_chunks(chunks, DB_DIR)

if __name__ == "__main__":
    run_ingestion()
