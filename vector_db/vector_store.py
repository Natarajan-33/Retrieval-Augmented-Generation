import streamlit as st
from langchain_chroma import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from typing import List, Tuple
from langchain.schema import Document
import logging



def addData(corpusData: List[Document]) -> Chroma:
    """
    Obtain GPT4AllEmbeddings and use it to embed the chunks, then store them in an open-source vector database called ChromaDB.

    Args:
        corpusData (List[Document]): A list of documents to be embedded and stored.

    Returns:
        Chroma: A Chroma database instance containing the embedded documents.
    """
    try:
        if "embedd" not in st.session_state:
            st.session_state.embedd = GPT4AllEmbeddings()
            logging.info("Initialized GPT4AllEmbeddings. fn=addData")

        # Create or update the Chroma database with the corpus data
        db = Chroma.from_documents(corpusData, st.session_state.embedd, persist_directory="./Vector_database/chroma_db1")
        logging.info(f"Chroma database created with {len(corpusData)} documents. fn=addData, directory=./Vector_database/chroma_db1")
        return db

    except Exception as e:
        logging.error(f"Error while adding data to Chroma database. fn=addData, error={e}")
        raise  # Re-raise the exception after logging

def find_match(query: str, k: int, db: Chroma) -> List[Tuple[Document, float]]:
    """
    Given a user query, use similarity search to find related chunks from the database.

    Args:
        query (str): The user query string.
        k (int): The number of top matches to retrieve.
        db (Chroma): The Chroma database instance to search in.

    Returns:
        List[Tuple[Document, float]]: A list of tuples containing the matching documents and their similarity scores.
    """
    try:
        # Perform similarity search
        retrieved_doc = db.similarity_search_with_score(query, k=k)
        logging.info(f"Similarity search performed. fn=find_match, query='{query}', k={k}, matches_found={len(retrieved_doc)}")
        return retrieved_doc

    except Exception as e:
        logging.error(f"Error during similarity search. fn=find_match, query='{query}', error={e}")
        raise  # Re-raise the exception after logging
