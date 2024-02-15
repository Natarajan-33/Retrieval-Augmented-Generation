import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings


def addData(corpusData):
    if "embedd" not in st.session_state:
        st.session_state.embedd = GPT4AllEmbeddings()
    db = Chroma.from_documents (corpusData, st.session_state.embedd, persist_directory = "./Vector_database/chroma_db1")
    return db


def find_match(query,k,db):
    retrieved_doc = db.similarity_search_with_score(query, k=k)
    return retrieved_doc