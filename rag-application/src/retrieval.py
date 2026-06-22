from config import OPENROUTER_API_KEY
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def get_retriever(db_path):
    """
    Initialize vector DB from disk and return a retriever object.
    """
    print(f"Loading retriever from vector DB at {db_path}...")
    
    # Re-initialize the same embedding function used during ingestion
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small", 
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )
    
    # Load the persisted vector database
    vectorstore = Chroma(
        persist_directory=str(db_path),
        embedding_function=embeddings
    )
    
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )
    return retriever

def retrieve_context(query, retriever, k=3):
    """
    Retrieve the top k most relevant document chunks matching the query.
    """
    print(f"Retrieving context for query: '{query}'...")
    contexts = retriever.invoke(query)
    print(f"Retrieved {len(contexts)} context chunks")
    return contexts
