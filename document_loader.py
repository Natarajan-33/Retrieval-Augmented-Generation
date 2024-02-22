from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import SeleniumURLLoader

# Function to load documents from a specified directory
def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents


# Function to split a list of documents into chunks
def split_docs(documents, chunk_size=1000, chunk_overlap=200):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs


# Function to scrape text content from a specified URL
def scrape_text_from_url(url):
    loader = SeleniumURLLoader(urls=[url])
    data = loader.load()
    docs = split_docs(data)
    return docs


# Function to scrape text content from documents in a specified directory
def scrape_text_from_doc(directory):
    documents = load_docs(directory)
    docs = split_docs(documents)
    return docs