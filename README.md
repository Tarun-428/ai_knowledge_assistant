# 🧠 AI Knowledge Assistant

An **enterprise-ready AI Knowledge Assistant** built with **FastAPI, LangGraph, RAG, Redis, and Supabase/PostgreSQL**.
This system allows users to **upload documents and interact with them using natural language**, powered by modern **Retrieval-Augmented Generation (RAG)** and **agentic workflows**.

The assistant can answer questions, summarize documents, and stream responses in real time through a **ChatGPT-like interface**.

---

# 🚀 Features

### 📄 Document Understanding

* Upload PDFs and documents
* Automatic chunking and embedding
* Semantic search using **Chroma vector database**

### 🔍 Retrieval-Augmented Generation (RAG)

* Context-aware answers from uploaded documents
* Cross-encoder **reranking** for better retrieval accuracy
* Query rewriting for improved results

### 🧠 Intelligent Query Routing (LangGraph)

The system automatically detects the user’s intent and routes queries to the correct pipeline:

| Query Type         | Pipeline                 |
| ------------------ | ------------------------ |
| Question answering | Vector search + LLM      |
| Document summary   | Map-Reduce summarization |
| General query      | Standard LLM generation  |

### ⚡ Real-Time Streaming

* Server-Sent Events (SSE)
* Token-by-token streaming like ChatGPT

### 🔐 Authentication & RBAC

* Secure login and registration
* JWT authentication
* Role-based access control

### 🗂 Conversation Memory

* Redis-based conversation memory
* Persistent chat sessions
* Context-aware follow-up questions

### 🛡 Guardrails (Enterprise Safety)

* Prompt injection detection
* Input validation
* Output grounding checks
* PII filtering

### 💬 Interactive Chat UI

* Dark themed ChatGPT-style interface
* Live streaming responses
* File upload interface
* Loading animations

---

# 🏗 Architecture

```
Frontend (HTML/CSS/JS)
        │
        ▼
FastAPI Backend
        │
        ▼
LangGraph Workflow
        │
 ┌───────────────┬───────────────┐
 │               │               │
RAG Pipeline   Summary Node   Safety Guardrails
 │               │
Vector DB     MapReduce
 │               │
LLM           LLM
        │
        ▼
Redis (Memory + Cache)
```

---

# 🛠 Tech Stack

### Backend

* **FastAPI**
* **LangChain**
* **LangGraph**
* **OpenAI / LLM APIs**
* **Chroma Vector Database**
* **Redis**

### Database

* **Supabase PostgreSQL**

### Frontend

* **HTML**
* **CSS**
* **JavaScript**
* **Streaming UI**

### AI Components

* Sentence Transformers
* Cross Encoder Reranking
* Retrieval-Augmented Generation
* Map-Reduce Summarization


---

# ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/Tarun-428/ai_knowledge_assistant.git

cd ai_knowledge_assistant
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Start Redis

```
redis-server
```

---

### 5️⃣ Configure environment variables

Create `.env` file:

```
OPENAI_API_KEY=your_key
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
```

---

### 6️⃣ Run the server

```
uvicorn app.main:app --reload
```

Open browser:

```
http://localhost:8000
```

---

# 📊 Example Workflow

1️⃣ User logs in
2️⃣ Uploads a document
3️⃣ System processes and stores embeddings
4️⃣ User asks a question
5️⃣ LangGraph routes query
6️⃣ RAG retrieves relevant chunks
7️⃣ LLM generates answer
8️⃣ Response streams live to UI
Hybrid search (BM25 + vector)


---

# 🔮 Future Improvements

* Multi-document comparison
* Knowledge graph integration
* Agentic research workflows
* Auto document classification
* Fine-tuned embedding models

---

# 📜 License

MIT License

---

# 🙌 Acknowledgements

This project uses open-source tools from:

* FastAPI
* LangChain
* LangGraph
* ChromaDB
* Redis
* OpenAI
* Supabase

---

# ⭐ If you like this project

Give it a **star on GitHub** ⭐
