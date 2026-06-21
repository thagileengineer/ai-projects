def construct_prompt(context, query):
    """
    Combine the context and query into a formatted prompt.
    """
    prompt = (
        f"You are a helpful assistant. Use the following context to answer the question.\n"
        f"Context: {context}\n"
        f"Question: {query}\n"
        f"Answer:"
    )
    return prompt

def generate_answer(prompt):
    """
    Call the LLM (Gemini or Groq) with the formatted prompt and return the result.
    """
    print("Generating answer from LLM...")
    # TODO: Initialize Gemini/Groq client and generate response
    return "This is a placeholder answer. Implement LLM API call in generation.py."
