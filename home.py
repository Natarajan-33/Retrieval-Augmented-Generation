import shutil
import streamlit as st
import os
from vector_store import *
import llm
from document_loader import *

# Set page layout to wide
st.set_page_config(page_title="RAG on our own data",layout="wide")

#Changing color of the streamlit sidebar
st.sidebar.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #6b5c4b; /* Replace with your desired color code */
        }
    </style>

""",unsafe_allow_html=True)

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
col1, col2, col3 = st.columns([0.5,3,0.5],gap="large")
with col2:
    st.header("Answering questions based on personal data sources.")
st.divider()

st.sidebar.subheader("Choose the data source")
data_source = st.sidebar.radio(
    '',
    ('URL','Local pdf files'), label_visibility="collapsed")

#Input Data Source
if data_source == "URL":
    url = st.sidebar.text_input("Enter the url of the document")
elif data_source == "Local pdf files":
    path = st.sidebar.text_input("Enter the local directory of the document")

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
    col1, col2, col3 = st.columns([1,3,1.5],gap="large")
    with col2:
        st.subheader("Please feed the document source to proceed further")

if st.session_state.database_loaded == True :
    col1, col2, col3 = st.columns([5,3,0.5],gap="large")
    with col1:
        st.subheader("Please enter your question")
        question = st.text_input("",label_visibility="collapsed")
        button = st.button("Submit the question")
    if question and button:
        with st.spinner("Searching for the answer..."):
            context = find_match(question,15,st.session_state.db)
            cleaned_context = ""
            for doc in context:
                string = doc[0].page_content.replace("\n\n"," ")
                cleaned_context += string + "\n\n"
            prompt = llm.create_prompt(cleaned_context,question)
            answer = llm.generate_answer(prompt)
            st.success("Answer: "+answer)
            st.divider()
            with st.container(height=600, border=False):
                st.expander("Click to expand actual retrieved documents").write(cleaned_context)

            


       