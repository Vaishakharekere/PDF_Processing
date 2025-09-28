# Simple RAG Chatbot

This is a Retrieval-Augmented Generation (RAG) chatbot application that answers user queries using the content of your own PDF documents. It uses FAISS for vector storage and Hugging Face models for embeddings and LLM responses.

## Features
- Loads and splits PDFs from the `data/` directory
- Stores document embeddings in a local FAISS vector store
- Retrieves relevant context for user queries
- Uses a language model to generate answers based only on your documents
- Interactive terminal chat interface

## Setup

### 1. Clone the repository
```
git clone https://github.com/Vaishakharekere/PDF_Processing.git
cd PDF_Processing
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Add your PDF documents
Place your PDF files in the `data/` directory. The app will automatically load and index them.


### 4. Configure Hugging Face API Token
Create a .env file in the root directory of the project.


- Add your Hugging Face API token to the .env file as follows
```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here || HF_TOKEN=your_huggingface_token_here
```

- **You should replace the value of `HF_TOKEN` with your own Hugging Face token for security and access.**
- You can change the model used in `llm.py` as well by passing valid REPO ID as parameter. Currently **HuggingFaceTB/SmolLM3-3B** model is used.

## Usage

### Run the chatbot
```
python main.py
```

### Options in the chat
- Type your question and press Enter to get an answer based on your documents.
- Type `exit` or `quit` to end the chat session.

## File Structure
- `main.py` — Entry point, runs the interactive chat
- `pdf_loader.py` — Loads and splits PDFs
- `vector_store.py` — Handles FAISS vector storage
- `retriever.py` — Retrieves relevant documents
- `llm.py` — Language model configuration
- `chatbot.py` — RAG chatbot logic
- `chatbot_utils.py` — Helper functions
- `data/` — Place your PDFs here

## Troubleshooting
- If you see errors about missing models or API keys, check your Hugging Face token in `.env` and model name in `llm.py`.
- If no documents are found, make sure your PDFs are in the `data/` folder.

# Example Queries & Responses

This file shows example interactions with the **Simple RAG Chatbot**, demonstrating how it retrieves answers from your PDF documents.

---

## **Query 1**  
- **Question:**  
What is the layer count, hidden size, and total parameters for BERT BASE and BERT LARGE?
- **Answer:**  
BERTBASE (L=12, H=768, A=12, Total Parameters=110M)
BERTLARGE (L=24, H=1024, A=16, Total Parameters=340M)



## **Query 2**  
- **Question:**  
Does BERT need a large amount of pre-training to achieve high fine-tuning accuracy?
- **Response:**  
Yes, BERT BASE achieves almost 1.0% additional accuracy on MNLI when trained on 1M steps compared to 500k steps.
