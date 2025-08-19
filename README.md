# Offline RAG App with Ollama

This is a Retrieval-Augmented Generation (RAG) app that works **offline**, using:

- **Ollama LLM**  
- **FAISS** for vector search  
- **MiniLM** embeddings (from Sentence-Transformers)  
- **Streamlit** as the web interface  


## Features

- Ask questions based on your local document corpus
- Fully offline — no external API required
- Lightweight and fast with precomputed embeddings


## Requirements

Install all required Python packages:

pip install -r requirements.txt

## Steps to install

- Install Ollama [Install Ollama](https://ollama.com/download)
- Install any model, visit [Ollama Model Downloads](https://github.com/ollama/ollama) for more information
- Verify Installation by running `ollama run [Your model name]`
- go to root directory and run `streamlit run app.py`
- upload file required and ask questions