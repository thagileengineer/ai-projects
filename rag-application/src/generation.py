from langchain_openai import ChatOpenAI
from config import OPENROUTER_API_KEY

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
    Call the LLM (OpenRouter/OpenAI) with the formatted prompt and return the result.
    """
    print("Generating answer from LLM...")

    model = ChatOpenAI(
        model="google/gemini-2.5-flash",
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0.7,
        max_tokens=1000,
    )
    response = model.invoke(prompt)
    return response.content
