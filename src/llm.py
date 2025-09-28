
# src/llm.py
import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

# Load environment variables into os.environ
load_dotenv() 

def createLLM(REPO_ID: str = "mistralai/Mistral-7B-Instruct-v0.3"): 
    try:
        # 1. Retrieve the token from the environment variables (loaded by load_dotenv)
        hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")

        if not hf_token:
            raise ValueError("HUGGINGFACEHUB_API_TOKEN is not set in the environment.")

        # 2. Use the retrieved variable 'hf_token'
        llm = HuggingFaceEndpoint(
            repo_id=REPO_ID,
            task="conversational",
            max_new_tokens=512,
            do_sample=False,
            repetition_penalty=1.03,
            huggingfacehub_api_token=hf_token 
        )

        chat_llm = ChatHuggingFace(llm=llm, verbose=True)
        print("LLM Initialized")
        return chat_llm
    except Exception as e:
        print(f"LLM Initialization failed: {str(e)}") 
        return None

chat_llm = createLLM(REPO_ID="HuggingFaceTB/SmolLM3-3B")