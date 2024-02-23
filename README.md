# Retrieval-Augmented-Generation

# Project Name: RAGExplorer

## Introduction

RAGExplorer is a robust and versatile RAG (Retrieval-Augmented Generation) application designed to seamlessly handle PDF documents from various sources. With a powerful combination of tools and technologies, including Documentary Loader, Recursive Text Splitter, GPT-4 Embedding, Chroma DB, and integration with the Gemini Pro LLM API, RAGExplorer offers an intuitive interface for extracting valuable insights from your knowledge sources.

### Key Features

- **URL and Local Path Support:** RAGExplorer accommodates both URL and local path inputs for PDF documents, providing flexibility in data sourcing.
  
- **Vector DB Creation:** The application efficiently creates a vector database from the loaded data, enabling efficient storage and retrieval of information.

- **Interactive Querying:** Users can leverage RAGExplorer to query over the provided data. The Gemini Pro LLM API responds with valuable insights, enhancing the depth of knowledge exploration.

### Streamlit UI

RAGExplorer comes equipped with a Streamlit-based user interface, ensuring a user-friendly experience while interacting with the application. The streamlined design facilitates easy navigation and efficient utilization of the application's capabilities.

## Installation

To get started with RAGExplorer, follow these simple installation steps:

```bash
# Clone the repository
[git clone https://github.com/yourusername/RAGExplorer.git](https://github.com/Natarajan-33/Retrieval-Augmented-Generation.git)
cd RAGExplorer

# Install dependencies
pip install -r requirements.txt
```

## Tools and Technologies

RAGExplorer harnesses the power of several cutting-edge tools and technologies:

- **Documentary Loader:** Loads PDF documents seamlessly.
- **Recursive Text Splitter:** Splits documents into chunks recursively for efficient processing.
- **GPT-4 Embedding:** Embeds document chunks into vectors for enhanced analysis.
- **Chroma DB:** Stores vectors for quick and reliable data retrieval.
- **Gemini Pro LLM API:** Integrates with the API to provide responses from the knowledge source.
- **Streamlit UI:** Offers an intuitive and visually appealing frontend for an enhanced user experience.

Certainly! If users encounter an error related to the "pwd" import in the `pebblo.py` file, you can include instructions in your README to guide them on resolving the issue. Here's a section you can add:

<font color="red"><h2>Troubleshooting</h2></font>

### ImportError: No module named 'pwd' in pebblo.py

If you encounter an `ImportError` related to the 'pwd' module in the `pebblo.py` file, you can try the following steps:

1. **Locate the pebblo.py file:**
   Navigate to the directory where the `pebblo.py` file is located. In a typical virtual environment setup, you can find it at:
   ```
   \venv\lib\site-packages\langchain_community\document_loaders\pebblo.py
   ```

2. **Comment out the problematic import statement:**
   Open the `pebblo.py` file and find the line that says `import pwd`. To comment out this line, add a `#` at the beginning of the line. It should look like this:
   ```python
   # import pwd
   ```

3. **Save the file:**
   Save the changes to the `pebblo.py` file.

4. **Run the script again:**
   Try running your script or application again and check if the error persists.

By commenting out the 'pwd' import statement, you are temporarily excluding it from the code execution. However, keep in mind that modifying third-party packages directly may not be a long-term solution, and it's recommended to check for updates or seek guidance from the package maintainers.

