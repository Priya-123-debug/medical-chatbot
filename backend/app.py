from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.rag import ask_question

app = FastAPI()

# Add this block to enable communication with your React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change "*" to "http://localhost:3000" for better security
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    answer = ask_question(query.question)
    return {"question": query.question, "answer": answer}