# Simple RAG System Demo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This project demonstrates a basic Retrieval-Augmented Generation (RAG) system using Python, Qdrant, Streamlit, and Ollama. It's designed to be easy to understand and set up, making it perfect for educational purposes.

## Features

- Upload PDF and TXT files to create a knowledge base
- Add URLs to scrape and index content
- Chat with your documents using Llama 3.2 1B model
- Simple and intuitive Streamlit interface
- Well-documented code for educational purposes

## Prerequisites

1. Python 3.8 or higher
2. Ollama installed and running locally
3. Qdrant running locally
4. Docker installed and running

## Quick Start

### For macOS/Linux Users:

1. Make the setup script executable:
   ```bash
   chmod +x setup.sh
   ```

2. Run the setup script:
   ```bash
   ./setup.sh
   ```

3. Start the application:
   ```bash
   ./start.sh
   ```

### For Windows Users:

1. Open PowerShell and run:
   ```powershell
   .\setup.ps1
   ```

2. Start the application:
   ```powershell
   .\start.ps1
   ```

## Manual Installation

If you prefer to set up manually:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/simple-rag-demo.git
   cd simple-rag-demo
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Ollama and pull the Llama 3.2 1B model:
   ```bash
   ollama pull llama2:1.3b
   ```

4. Start Qdrant locally:
   ```bash
   docker run -p 6333:6333 qdrant/qdrant
   ```

## Project Structure

```
simple-rag-demo/
├── app.py                 # Main Streamlit application
├── document_processor.py  # Handles document loading and processing
├── vector_store.py       # Manages the Qdrant vector database
├── rag_system.py         # Core RAG implementation
├── tutorial.ipynb        # Jupyter notebook explaining the project
├── setup.sh              # Setup script for macOS/Linux
├── setup.ps1             # Setup script for Windows
├── start.sh              # Start script for macOS/Linux
├── start.ps1             # Start script for Windows
├── requirements.txt      # Python dependencies
├── example.txt           # Example document for testing
├── README.md             # Project documentation
└── LICENSE               # MIT License
```

## Usage

1. Start the Streamlit app using the start script or manually:
   ```bash
   streamlit run app.py
   ```

2. Open your browser to the provided local URL

3. Try the example document:
   - Upload `example.txt`
   - Ask questions like "What are the key features?"

4. Add your own documents:
   - Upload PDF or TXT files
   - Add URLs to scrape
   - Start chatting with your documents!

## Educational Resources

Check out the `tutorial.ipynb` notebook for a detailed explanation of how the RAG system works, including:
- Document processing
- Vector embeddings
- Retrieval mechanisms
- Response generation
- System architecture

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Ollama](https://ollama.ai) for the language model
- [Qdrant](https://qdrant.tech) for the vector database
- [Streamlit](https://streamlit.io) for the web interface
- [LangChain](https://www.langchain.com) for the RAG framework 