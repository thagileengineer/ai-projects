from src.config import DB_DIR

def get_retriever(db_path):
    """
    Initialize vector DB and return a retriever object.
    """
    print(f"Loading retriever from vector DB at {db_path}...")
    # TODO: Load Chroma database and return as retriever
    return None

def retrieve_context(query, retriever, k=3):
    """
    Retrieve the top k most relevant document chunks matching the query.
    """
    print(f"Retrieving context for query: '{query}'...")
    # TODO: Use similarity search on retriever to fetch documents
    contexts = []
    return contexts
