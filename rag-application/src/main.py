from src.config import DB_DIR
from src.retrieval import get_retriever, retrieve_context
from src.generation import construct_prompt, generate_answer

def run_rag_query(query):
    # 1. Load retriever
    retriever = get_retriever(DB_DIR)
    
    # 2. Retrieve relevant context
    contexts = retrieve_context(query, retriever)
    context_str = "\n".join([doc.page_content for doc in contexts]) if contexts else "No context found."
    
    # 3. Build prompt
    prompt = construct_prompt(context_str, query)
    
    # 4. Generate answer
    answer = generate_answer(prompt)
    
    return answer

if __name__ == "__main__":
    # Test query
    user_query = "What is Retrieval-Augmented Generation?"
    print(f"Query: {user_query}")
    answer = run_rag_query(user_query)
    print(f"Answer: {answer}")
