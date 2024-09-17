from typing import List
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import SeleniumURLLoader
from langchain.schema import Document

def load_docs(directory: str) -> List[Document]:
    """
    Load documents from the specified directory.

    Args:
        directory (str): The path to the directory containing documents.

    Returns:
        List[Document]: A list of loaded documents.
    """
    loader = DirectoryLoader(directory)
    documents = loader.load()
    return documents

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
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

def scrape_text_from_url(url: str) -> List[Document]:
    """
    Scrape text content from a specified URL.

    Args:
        url (str): The URL to scrape.

    Returns:
        List[Document]: A list of documents containing the scraped text chunks.
    """
    loader = SeleniumURLLoader(urls=[url])
    data = loader.load()
    docs = split_docs(data)
    return docs

def scrape_text_from_doc(directory: str) -> List[Document]:
    """
    Scrape text content from documents in a specified directory.

    Args:
        directory (str): The path to the directory containing documents.

    Returns:
        List[Document]: A list of documents containing the text chunks from the directory.
    """
    documents = load_docs(directory)
    docs = split_docs(documents)
    return docs
