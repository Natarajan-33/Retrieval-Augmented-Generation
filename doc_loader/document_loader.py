from typing import List
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import SeleniumURLLoader
from langchain.schema import Document
import logging


def load_docs(directory: str) -> List[Document]:
    """
    Load documents from the specified directory.

    Args:
        directory (str): The path to the directory containing documents.

    Returns:
        List[Document]: A list of loaded documents.
    """
    try:
        loader = DirectoryLoader(directory)
        documents = loader.load()
        logging.info(f"Documents loaded successfully. fn=load_docs, directory={directory}, num_documents={len(documents)}")
        return documents
    except Exception as e:
        logging.error(f"Error loading documents. fn=load_docs, directory={directory}, error={e}")
        raise  # Re-raise the exception after logging

def split_docs(documents: List[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
    """
    Split a list of documents into smaller chunks.

    Args:
        documents (List[Document]): The documents to split.
        chunk_size (int, optional): The maximum size of each chunk. Defaults to 1000.
        chunk_overlap (int, optional): The number of overlapping characters between chunks. Defaults to 200.

    Returns:
        List[Document]: A list of split document chunks.
    """
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        docs = text_splitter.split_documents(documents)
        logging.info(f"Documents split into chunks. fn=split_docs, chunk_size={chunk_size}, chunk_overlap={chunk_overlap}, num_chunks={len(docs)}")
        return docs
    except Exception as e:
        logging.error(f"Error splitting documents. fn=split_docs, chunk_size={chunk_size}, chunk_overlap={chunk_overlap}, error={e}")
        raise  # Re-raise the exception after logging

def scrape_text_from_url(url: str) -> List[Document]:
    """
    Scrape text content from a specified URL.

    Args:
        url (str): The URL to scrape.

    Returns:
        List[Document]: A list of documents containing the scraped text chunks.
    """
    try:
        loader = SeleniumURLLoader(urls=[url])
        data = loader.load()
        logging.info(f"Text scraped from URL successfully. fn=scrape_text_from_url, url={url}, num_documents={len(data)}")
        docs = split_docs(data)
        logging.info(f"Scraped text split into chunks. fn=scrape_text_from_url, url={url}, num_chunks={len(docs)}")
        return docs
    except Exception as e:
        logging.error(f"Error scraping text from URL. fn=scrape_text_from_url, url={url}, error={e}")
        raise  # Re-raise the exception after logging

def scrape_text_from_doc(directory: str) -> List[Document]:
    """
    Scrape text content from documents in a specified directory.

    Args:
        directory (str): The path to the directory containing documents.

    Returns:
        List[Document]: A list of documents containing the text chunks from the directory.
    """
    try:
        documents = load_docs(directory)
        logging.info(f"Documents scraped from directory successfully. fn=scrape_text_from_doc, directory={directory}, num_documents={len(documents)}")
        docs = split_docs(documents)
        logging.info(f"Scraped documents split into chunks. fn=scrape_text_from_doc, directory={directory}, num_chunks={len(docs)}")
        return docs
    except Exception as e:
        logging.error(f"Error scraping text from documents in directory. fn=scrape_text_from_doc, directory={directory}, error={e}")
        raise  # Re-raise the exception after logging