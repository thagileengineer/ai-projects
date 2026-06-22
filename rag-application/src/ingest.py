from pathlib import Path
import os
from config import DATA_DIR, DB_DIR, CHUNK_SIZE, CHUNK_OVERLAP, OPENROUTER_API_KEY
from langchain_community.document_loaders import TextLoader, PyPDFLoader, AsyncHtmlLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma.vectorstores import Chroma

def load_documents(directory_path, filename=None):
    """
    Load files (PDFs, text files, HTML) from the specified directory.
    """
    print(f"Loading documents from {directory_path}...")
    
    pages = []
    if filename:
        file_path = Path(directory_path) / filename
        if file_path.suffix == ".pdf":
            loader = PyPDFLoader(file_path)
            pages.extend(loader.load())
        elif file_path.suffix == ".txt":
            loader = TextLoader(file_path)
            pages.extend(loader.load())
        elif file_path.suffix == ".html":
            loader = AsyncHtmlLoader(file_path)
            pages.extend(loader.load())
    else:
        for filename in os.listdir(directory_path):
            file_path = Path(directory_path) / filename
            if file_path.suffix == ".pdf":
                loader = PyPDFLoader(file_path)
                pages.extend(loader.load())
            elif file_path.suffix == ".txt":
                loader = TextLoader(file_path)
                pages.extend(loader.load())
            elif file_path.suffix == ".html":
                loader = AsyncHtmlLoader(file_path)
                pages.extend(loader.load())
    
    print(f"[Loading Phase] Loaded {len(pages)} pages from {directory_path}")
    
    return pages

def split_documents(documents):
    """
    Split documents into smaller semantic chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"[Splitting Phase] Split {len(chunks)} chunks from {len(documents)} pages")
    
    return chunks


def metadata_tagging(chunks):
    for i, chunk in enumerate(chunks):
        chunk.metadata['chunk_id']= f"CHK-{i + 1:03d}"
        chunk.metadata['project_name'] = "Angular Architecture"


def index_chunks(chunks, db_path):
    """
    Vectorize chunks and save them into the Chroma vector database.
    """
    print(f"Indexing chunks in database at {db_path}...")
    # 2. Embedding Setup
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small", 
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )

    input_text = "The meaning of life is 42"
    sample_vector = embeddings.embed_query("hello")
    print(sample_vector[:3])
    print("Embedding generated successfully!")
    
    vectorstore = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings,
        persist_directory=str(db_path)
    )

    print(f"\n[Embedding & Indexing Phase] Indexed {len(chunks)} chunks into Chroma DB at {db_path}")
    pass

def run_ingestion():
    docs = load_documents(DATA_DIR, filename="Angular Signals Architecture.txt")
    chunks = split_documents(docs)
    metadata_tagging(chunks)
    index_chunks(chunks, DB_DIR)

if __name__ == "__main__":
    run_ingestion()
