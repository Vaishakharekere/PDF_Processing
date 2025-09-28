# src/vector_store.py
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from typing import List, Optional
import os
import pickle

embeddings = HuggingFaceEmbeddings()

VECTORSTORE_PATH = os.path.join(os.path.dirname(__file__), "faiss_index")

def create_vectorstore(documents: List[Document]) -> Optional[FAISS]:
    """
    Create a FAISS vector store from a list of documents.
    """
    try:
        vector_store = FAISS.from_documents(documents, embeddings)
        # Save the index for persistence
        vector_store.save_local(VECTORSTORE_PATH)
        return vector_store
    except Exception as e:
        print(f"Error creating FAISS vector store: {e}")
        return None

def load_vectorstore() -> Optional[FAISS]:
    """
    Load a FAISS vector store from disk if it exists.
    """
    try:
        if os.path.exists(VECTORSTORE_PATH):
            return FAISS.load_local(VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True)
        else:
            print("No FAISS index found. Please create one first.")
            return None
    except Exception as e:
        print(f"Error loading FAISS vector store: {e}")
        return None

def store_in_vectorstore(documents: List[Document]) -> bool:
    """
    Add documents to the FAISS vector store, creating it if needed.
    """
    try:
        vector_store = load_vectorstore()
        if vector_store is None:
            vector_store = create_vectorstore(documents)
            if vector_store is None:
                raise Exception("Failed to create FAISS vector store.")
            print(f"Created new FAISS vector store with {len(documents)} documents.")
        else:
            vector_store.add_documents(documents)
            vector_store.save_local(VECTORSTORE_PATH)
            print(f"Added {len(documents)} documents to existing FAISS vector store.")
        return True
    except Exception as e:
        print(f"Error storing documents in FAISS vector store: {e}")
        return False