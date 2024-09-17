import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(override=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def create_prompt(context: str, query: str) -> str:
    """
    Create a prompt by combining the user query with the retrieved context.

    Args:
        context (str): The context to be included in the prompt.
        query (str): The user's query.

    Returns:
        str: The formatted prompt string.
    """
    header = (
        "Please carefully respond to the prompts based on the provided context. "
        "Be truthful and specific in your answers. If the given context is insufficient "
        "to address a prompt, kindly request additional clarification from the user. "
        "Avoid making assumptions or providing inaccurate information. Your cooperation "
        "ensures the accuracy and relevance of the responses. Never provide information "
        "that is not grounded in the available context."
    )
    return (
        f"Assistant behavior : {header} \n\n Provided context : {context}  \n\n  User Prompt : {query} "
    )

def generate_answer(prompt: str) -> str:
    """
    Call Google's Gemini Pro API to retrieve the answer.

    Args:
        prompt (str): The prompt to be sent to the model.

    Returns:
        str: The generated answer from the model.
    """
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    answer = response.text
    return answer
