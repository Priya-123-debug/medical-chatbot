
import os
import sys
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from src.helper import (
    load_pdf_files,
    text_split,
    get_embeddings
)

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

index_name = "medical-chatbot"

documents = load_pdf_files("data")
chunks = text_split(documents)

embedding = get_embeddings()

pc = Pinecone(api_key=PINECONE_API_KEY)

existing_indexes = [idx["name"] for idx in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

docsearch = PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embedding,
    index_name=index_name
)

print("Vector Store Created Successfully")
