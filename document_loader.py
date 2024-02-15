from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import SeleniumURLLoader


def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents


def split_docs(documents, chunk_size=200, chunk_overlap=200):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs


def scrape_text_from_url(url):
    loader = SeleniumURLLoader(urls=[url])
    data = loader.load()
    docs = split_docs(data)
    return docs

