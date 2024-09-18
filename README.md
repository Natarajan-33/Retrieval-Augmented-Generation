# TextLens: Retrieval-Augmented Generation Application

![TextLens App](https://github.com/user-attachments/assets/fc0b1c90-b76e-4f1b-a09a-667ccdaaf5e3)

## Table of Contents

- [Introduction](#introduction)
  - [Key Features](#key-features)
  - [Streamlit UI](#streamlit-ui)
- [Installation](#installation)
- [Tools and Technologies](#tools-and-technologies)
- [Troubleshooting](#troubleshooting)
  - [1. Installation Error with ChromaDB](#1-installation-error-with-chromadb)
  - [2. ImportError: No module named 'pwd' in pebblo.py](#2-importerror-no-module-named-pwd-in-pebblopy)
- [Contributing](#contributing)

## Introduction

TextLens is a robust and versatile Retrieval-Augmented Generation (RAG) application designed to seamlessly handle PDF documents from various sources. By combining powerful tools and technologies—including Document Loaders, Recursive Text Splitter, GPT-4 Embeddings, ChromaDB, and integration with the Gemini Pro LLM API—TextLens offers an intuitive interface for extracting valuable insights from your knowledge sources.

### Key Features

- **URL and Local Path Support:** Accommodates both URL and local path inputs for PDF documents, providing flexibility in data sourcing.
- **Vector Database Creation:** Efficiently creates a vector database from the loaded data, enabling quick storage and retrieval of information.
- **Interactive Querying:** Allows users to query over the provided data. The Gemini Pro LLM API responds with valuable insights, enhancing knowledge exploration.

### Streamlit UI

TextLens comes equipped with a Streamlit-based user interface, ensuring a user-friendly experience while interacting with the application. The streamlined design facilitates easy navigation and efficient utilization of the application's capabilities.

## Installation

To get started with TextLens, follow these steps:

```bash
# Clone the repository
git clone https://github.com/Natarajan-33/Retrieval-Augmented-Generation.git
cd Retrieval-Augmented-Generation

# Create a virtual environment (recommended)
python -m venv rag_env

# Activate the virtual environment
# On Windows:
rag_env\Scripts\activate
# On macOS/Linux:
source rag_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

## Tools and Technologies

TextLens harnesses the power of several cutting-edge tools and technologies:

- **Document Loaders:** Load PDF documents seamlessly.
- **Recursive Text Splitter:** Splits documents into chunks recursively for efficient processing.
- **GPT-4 Embeddings:** Embeds document chunks into vectors for enhanced analysis.
- **ChromaDB:** Stores vectors for quick and reliable data retrieval.
- **Gemini Pro LLM API:** Although we have chosen to integrate with Gemini Pro LLM API for its free availability, we recommend considering GPT models, which tend to offer better performance in many cases.
- **Streamlit UI:** Offers an intuitive and visually appealing frontend for an enhanced user experience.

## Troubleshooting

### 1. Installation Error with ChromaDB

If you encounter an error related to installing `chroma-hnswlib` while setting up ChromaDB, similar to:

```
ERROR: Failed building wheel for chroma-hnswlib
...
fatal error C1083: Cannot open include file: 'crtdbg.h': No such file or directory
```

**Cause:** This error occurs because `chroma-hnswlib` requires compiling C++ extensions, which need Microsoft Visual C++ Build Tools on Windows.

#### **Solution: Install Microsoft Visual C++ Build Tools.** [Look at the issue in GitHub](https://github.com/chroma-core/chroma/issues/189#issuecomment-1454418844)

1. **Download Build Tools:**

   - Visit the [Microsoft Visual C++ Build Tools download page](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
   - Click on **"Download Build Tools"**.

2. **Install Required Components:**

   - Run the installer (`vs_buildtools.exe`).
   - Select **"Desktop development with C++"** workload.
   - select **"MSVC v143 - VS 2022 C++ x64/x86 build tools (Latest)"** and the **"Windows 10 SDK"** or **"Windows 11 SDK"** as per your system.
   - Click **"Install"** and wait for the installation to complete.

3. **Restart Your Computer:**

   - It's recommended to restart your computer after installation.

4. **Re-attempt Installation:**

   - Activate your virtual environment if not already active.
   - Run:

     ```bash
     pip install chromadb
     ```

#### **Alternative Solution: Use FAISS Instead of ChromaDB**

If the problem persists after installing the build tools, you can use FAISS as an alternative vector store.

1. **Install FAISS:**

   ```bash
   pip install faiss-cpu
   ```

2. **Modify Your Code:**

   - Update your code to use FAISS instead of ChromaDB for vector storage.
   - Refer to the [FAISS documentation](https://github.com/facebookresearch/faiss) for more details.

### 2. ImportError: No module named 'pwd' in pebblo.py

If you encounter an `ImportError` related to the `pwd` module in the `pebblo.py` file:

```
ImportError: No module named 'pwd'
```

**Cause:** This error occurs because the `pwd` module is specific to Unix/Linux systems and is not available on Windows.

#### **Solution: Comment Out the Problematic Import**

1. **Locate the `pebblo.py` File:**

   The file is typically located at:

   ```
   <your_virtual_env>\lib\site-packages\langchain_community\document_loaders\pebblo.py
   ```

2. **Comment Out the `import pwd` Line:**

   Open `pebblo.py` in a text editor and locate the line:

   ```python
   import pwd
   ```

   Add a `#` at the beginning to comment it out:

   ```python
   # import pwd
   ```

3. **Save the File:**

   Save the changes to `pebblo.py`.

4. **Run Your Application Again:**

   Try running your application to see if the error is resolved.

**Note:** Modifying third-party library code is generally not recommended as a long-term solution. Check for updates to the `langchain_community` package or consider reporting the issue to the maintainers.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
