import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv(override=True)

GEMINI_API_KEY =os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Create a prompt by combining the user query with the retrieved context.
def create_prompt(context,query):
    # header = "Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text and requires some latest information to be updated, print 'Sorry Not Sufficient context to answer query' \n"
    header = "Please carefully respond to the prompts based on the provided context. Be truthful and specific in your answers. If the given context is insufficient to address a prompt, kindly request additional clarification from the user. Avoid making assumptions or providing inaccurate information. Your cooperation ensures the accuracy and relevance of the responses. Never provide information that is not grounded in the available context."
    return f"Assistant behavior : {header} \n\n Provided context : {context}  \n\n  User Prompt : {query} "

# Call Google's Gemini Pro API to retrieve the answer.
def generate_answer(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    answer = response.text
    return answer

