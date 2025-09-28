# main.py
import os
from src.pdf_loader import load_and_split_pdf
from src.vector_store import store_in_vectorstore, load_vectorstore
from src.retriever import create_retriever
from src.chatbot_utils import docs_to_str
from src.chatbot import rag_chatbot

def initialize_vectorstore():
    pdf_dir = os.path.join(os.path.dirname(__file__), "data")
    print(f"Loading and splitting PDFs from {pdf_dir} ...")
    docs = load_and_split_pdf(pdf_dir)
    if not docs:
        print("No documents loaded from PDF.")
        return False
    success = store_in_vectorstore(docs)
    if not success:
        print("Failed to store documents in vector store.")
        return False
    print("Vector store initialized.")
    return True

async def main():
    # Step 1: Ensure vectorstore exists
    if not load_vectorstore():
        if not initialize_vectorstore():
            return

    # Step 2: Create retriever
    retriever = await create_retriever()
    if not retriever:
        print("Failed to create retriever.")
        return

    # Step 3: Interactive chat loop
    chat_history = []
    print("Welcome to the RAG Chatbot! Type 'exit' to quit.")
    while True:
        user_query = input("\nYou: ")
        if user_query.strip().lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Retrieve relevant docs
        docs = await retriever.ainvoke(user_query)
        print("context: \n")
        for i,doc in enumerate(docs):
            print(f"Context-{i+1}: \nContent: {doc.page_content}\nMetadata: {doc.metadata}\n\n")
        context = docs_to_str(docs)

        # Prepare input for the chain
        chain_input = {
            "context": context,
            "chat_history": "\n".join([f"User: {q}\nBot: {a}" for q, a in chat_history]),
            "query": user_query
        }

        # Get response from RAG chatbot
        try:
            response = rag_chatbot.invoke(chain_input)
        except Exception as e:
            print(f"Error during chatbot response: {e}")
            continue

        print(f"Bot: {response}")
        chat_history.append((user_query, response))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())