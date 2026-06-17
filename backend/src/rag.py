import os
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from src.helper import get_embeddings

# Load environment variables
load_dotenv()

# ---------------------------
# INITIALIZATION
# ---------------------------
embedding = get_embeddings()
index_name = "medical-chatbot"

# Connect to existing index
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding
)

retriever = docsearch.as_retriever(search_kwargs={"k": 5})

# Load Model & Tokenizer
# Note: Loading these globally makes the API faster to respond
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# ---------------------------
# RAG FUNCTION
# ---------------------------
def ask_question(question: str):
    # 1. Retrieve relevant docs
    retrieved_docs = retriever.invoke(question)

    # 2. Build context
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    # 3. Formatted Prompt
    prompt = f"""
You are a medical diagnostic assistant. 
When asked for 'diagnostic criteria', explain the specific test, the clinical values, or the symptoms required to confirm the diagnosis. 
Do not just provide a single word or a test name. Provide a complete, professional explanation based on the context.

Context:
{context}

Question:
{question}

Detailed Answer:
""".strip()
    
   

    # 4. Tokenize and Generate
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=2048
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=False  # Deterministic output
    )
    

    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()