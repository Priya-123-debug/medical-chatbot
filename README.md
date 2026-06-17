# 🏥 Medical Chatbot (RAG + FastAPI + Pinecone)

## 📌 Project Overview

Yeh project ek **Medical AI Chatbot** hai jo user ke questions ka answer deta hai using **Retrieval Augmented Generation (RAG)**.

Isme system pehle medical documents se relevant information retrieve karta hai (Pinecone vector database se), aur phir usko AI model (FLAN-T5) use karke simple language me answer generate karta hai.

---

## ⚙️ Tech Stack

* Python 🐍
* FastAPI ⚡
* LangChain 🧠
* Pinecone Vector DB 📦
* HuggingFace Transformers 🤗
* FLAN-T5 Model 🤖
* React (Frontend) 🌐

---

## 🧠 How It Works (Simple Flow)

1. User question input karta hai
2. Question embeddings me convert hota hai
3. Pinecone se similar medical documents retrieve hote hain
4. Retrieved context + question LLM ko diya jata hai
5. Model final answer generate karta hai

---

## 📁 Project Structure

```
medical-chatbot/
│
├── backend/
│   ├── app.py
│   ├── src/
│   │   ├── rag.py
│   │   ├── helper.py
│   │   ├── prompt.py
│   ├── data/
│   ├── store_index.py
│   ├── requirements.txt
│
├── frontend/
│   ├── (React app)
│
└── README.md
```

---

## 🚀 How to Run Backend

### 1️⃣ Environment Activate karo

```bash
conda activate medibot
```

OR (venv use kar rahe ho to)

```bash
.venv\Scripts\activate
```

---

### 2️⃣ Backend folder me jao

```bash
cd backend
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run server

```bash
python -m uvicorn app:app --reload
```

---

### 🌐 API URL

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Test API

### POST /ask

Example request:

```json
{
  "question": "What is diabetes?"
}
```

Example response:

```json
{
  "question": "What is diabetes?",
  "answer": "Diabetes is a medical condition where blood sugar level becomes high..."
}
```

---

## ⚠️ Common Issues

### ❌ Uvicorn not found

✔ Fix:

```bash
pip install uvicorn
```

---

### ❌ Module not found error

✔ Fix:

```bash
pip install -r requirements.txt
```

---

### ❌ Empty / weird answers

✔ Reason:

* Poor retrieval
* Small model (FLAN-T5 base)

---

## 📌 Future Improvements

* Better LLM (Llama / Mistral)
* Better chunking strategy
* UI chatbot interface (React)
* Streaming responses
* Medical safety filters

---

## 👨‍💻 Author

Built by: Supriya buddy 😄

---

## 💡 Note

Ye chatbot educational purpose ke liye hai. Medical advice ke liye real doctor consult karein.
