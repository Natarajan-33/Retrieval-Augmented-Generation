import shutil
import streamlit as st
import os
from vector_db.vector_store import *
from llm_model.llm import *
from doc_loader.document_loader import *

# Set page layout to wide
st.set_page_config(page_title="TextLens", page_icon="assets/logo.png", layout="wide")


# Load the CSS file
def load_css(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Call the function to load the styles
load_css("static\styles.css")


# Now render the text with the CSS class applied
st.sidebar.markdown(
    """
    <div class="header">
        TextLens
    </div>
    """,
    unsafe_allow_html=True
)


st.sidebar.divider()


url = False
path = False

# Initialize a database variable in the session state.
if "db" not in st.session_state:
    st.session_state.db = None

#Creating "Vector_database" folder to store embeddings
if "database_loaded" not in st.session_state:
    st.session_state.database_loaded = False
    folder_path = "./Vector_database"
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Add content to the user interface.
col1, col2, col3 = st.columns([1.1,3,0.5],gap="large")
with col2:
    st.header("Your Personalized AI Chatbot Assistant.🤖")
st.divider()

st.sidebar.subheader("Choose the data source")
data_source = st.sidebar.radio(
    '',
    ('URL','Local pdf files'), label_visibility="collapsed")

#Input Data Source
if data_source == "URL":
    url = st.sidebar.text_input("Enter the url of the document", key="url")
elif data_source == "Local pdf files":
    path = st.sidebar.text_input("Enter the local directory of the document", key="path")

# To fetch data from the source, chunk it, embed it, and store it in the database.
button = st.sidebar.button("Update Database")
if button and (url or path):
    with st.spinner("Updating Database..."):
        if url:
            corpusData = scrape_text_from_url(url)
        if path:
            corpusData = scrape_text_from_doc(path)
        # st.write(corpusData)
        st.session_state.db = addData(corpusData)
        st.session_state.database_loaded = True
        st.success("Database Updated")


if st.session_state.database_loaded == False:
    col1, col2, col3 = st.columns([1.4,3,0.5], gap="large")
    with col2:
        st.subheader("Please feed the document source to proceed further")

if st.session_state.database_loaded == True:
    # Initialize messages if not already in session_state
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display the chat messages
    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.chat_message("user").markdown(message['content'])
        else:
            st.chat_message("assistant").markdown(message['content'])
    
    # Get user input via the chat input UI element
    question = st.chat_input("Please enter your question")
    if question:
        # Add user's message to chat history
        st.session_state.messages.append({'role': 'user', 'content': question})
        # Display user's message
        st.chat_message("user").markdown(question)
        
        with st.spinner("Searching for the answer..."):
            # Retrieve matching documents from the database based on the question
            context = find_match(question, 15, st.session_state.db)
            cleaned_context = ""
            for doc in context:
                string = doc[0].page_content.replace("\n\n", " ")
                cleaned_context += string + "\n\n"
            
            # Prepare the prompt, including the last 7 messages for context
            history = st.session_state.messages[-7:]
            prompt = create_prompt_with_history(cleaned_context, question, history)
            
            # Generate an answer using the prompt
            answer = generate_answer(prompt)
            # Add assistant's message to chat history
            st.session_state.messages.append({'role': 'assistant', 'content': answer})
            # Display assistant's message
            st.chat_message("assistant").markdown(answer)
            
            st.divider()
            # Provide an expandable container to show the actual retrieved documents
            with st.expander("Click to expand actual retrieved documents"):
                st.write(cleaned_context)


            


       