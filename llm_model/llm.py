import os
from dotenv import load_dotenv
import google.generativeai as genai
import logging

# Load environment variables
try:
    load_dotenv(override=True)
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    if GEMINI_API_KEY:
        # Configure the API key
        genai.configure(api_key=GEMINI_API_KEY)
        logging.info("API key configured successfully.")
    else:
        logging.error("GEMINI_API_KEY is not set in the environment variables.")
        # Raise an exception to halt execution
        raise RuntimeError("API key configuration failed.")
    
except Exception as e:
    logging.error(f"Error loading environment variables or configuring API key. error={e}")
    raise  # Re-raise the exception to halt execution


def create_prompt_with_history(context: str, query: str, history: list[dict]) -> str:
    """
    Create a prompt by combining the user query, conversation history, and the retrieved context.

    Args:
        context (str): The context to be included in the prompt.
        query (str): The user's current query.
        history (list[dict]): The conversation history.

    Returns:
        str: The formatted prompt string including the conversation history.
    """
    try:
        header = (
            "Please carefully respond to the prompts based on the provided context. "
            "Be truthful and specific in your answers. If the given context is insufficient "
            "to address a prompt, kindly request additional clarification from the user. "
            "Avoid making assumptions or providing inaccurate information. Your cooperation "
            "ensures the accuracy and relevance of the responses. Never provide information "
            "that is not grounded in the available context."
        )
        
        # Build the conversation history
        history_text = ""
        for message in history:
            role = "User" if message['role'] == 'user' else "Assistant"
            content = message['content']
            history_text += f"{role}: {content}\n"
        
        # Combine everything into the prompt
        prompt = (
            f"Assistant behavior:\n{header}\n\n"
            f"Provided context:\n{context}\n\n"
            f"Conversation history:\n{history_text}\n"
            f"User Prompt:\n{query}"
        )
        logging.info(f"Prompt created successfully. fn=create_prompt_with_history, query='{query}', history_length={len(history)}")
        return prompt
    
    except Exception as e:
        logging.error(f"Error creating prompt. fn=create_prompt_with_history, error={e}")
        raise  # Re-raise the exception after logging


def generate_answer(prompt: str) -> str:
    """
    Call Google's Gemini Pro API to retrieve the answer.

    Args:
        prompt (str): The prompt to be sent to the model.

    Returns:
        str: The generated answer from the model.
    """
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        answer = response.text
        logging.info(f"Generated answer successfully. fn=generate_answer")
        return answer

    except Exception as e:
        logging.error(f"Error generating answer. fn=generate_answer, error={e}")
        raise  # Re-raise the exception after logging
