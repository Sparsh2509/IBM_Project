# 📧 AI Email Copilot using RAG

An AI-powered Email Generator built using **Retrieval-Augmented Generation (RAG)**.  
By combining semantic template retrieval via Google Gemini Embeddings with the reasoning power of the latest Google Gemini LLM, this system crafts highly personalized, context-aware professional emails tailored to any specific scenario, role, or tone.

* **Live UI Demo (Streamlit Cloud):** [https://ibmproject-gruy5zavcwsnugwcwwx9js.streamlit.app/](https://ibmproject-gruy5zavcwsnugwcwwx9js.streamlit.app/) 
* **Live REST API (AWS Elastic Beanstalk):** [http://Ai-email-copilot-env.eba-qtnai9na.us-east-1.elasticbeanstalk.com](http://Ai-email-copilot-env.eba-qtnai9na.us-east-1.elasticbeanstalk.com)

---

## 🚀 Features

- **Personalized Email Generation:** Generate highly targeted professional emails (Cold Email, Internship Request, Follow-up, Apology, Sales Outreach).
- **RAG-Powered:** Retrieve the most contextually relevant email templates from a local knowledge base to inject formatting & tone guidelines into the generator.
- **Fast FAISS Index:** Search and fetch semantic templates via highly efficient local FAISS vector search.
- **Gemini Embedding API:** Utilizes `gemini-embedding-2` for 3072-dimensional semantic search with zero local resource/RAM overhead.
- **Gemini 3.5 Flash Model:** Generates highly structured, natural, and tone-accurate copy.
- **FastAPI Layer:** Backend RAG pipeline exposed as REST endpoint and hosted on AWS Elastic Beanstalk (AL2023).

---

## 🏗 Architecture

```
User Input (UI / API Request)
        ↓
Generate Semantic Query
        ↓
Google Gemini Embeddings (3072-D)
        ↓
FAISS Vector Similarity Search
        ↓
Retrieve Top-K Context Templates
        ↓
Inject Context & Structuring into Prompt Template
        ↓
Google Gemini 3.5 Flash LLM Generates Final Email
```

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** (Frontend UI)
- **FastAPI** (REST Backend API)
- **LangChain** (RAG Orchestration)
- **Google Gemini Embeddings** (`gemini-embedding-2`)
- **FAISS** (Local Vector Database)
- **Google Gemini LLM** (`gemini-3.5-flash`)
- **AWS Elastic Beanstalk** (Cloud Hosting for FastAPI API)

---

## 📂 Project Structure

```
AI_Email_Generator/
│
├── streamlit_app.py            # Streamlit UI for generating emails via Live AWS API
├── app.py                      # CLI-based email generation interface
├── api.py                      # FastAPI REST endpoint exposing RAG pipeline
│
├── rag/
│   ├── build_vectorstore.py    # Builds FAISS vector index using Google GenAI embeddings
│   ├── retriever.py            # Handles vector search to retrieve relevant email templates
│
├── prompts/
│   ├── email_prompt.py         # Builds structured instruction prompt for Gemini LLM
│
├── Email_Templates_idea/       # Raw knowledge base of custom email templates
├── faiss_index/                # Stored FAISS binary vector database index files
├── requirements.txt            # Main Streamlit Cloud dependencies
├── requirements-api.txt        # Lightweight FastAPI dependencies for AWS EB
├── Procfile                    # Tells AWS Elastic Beanstalk how to run the FastAPI app
└── README.md                   # Project documentation
```

---

## 🔌 REST API (AWS Elastic Beanstalk)

The RAG pipeline is exposed as a live REST API endpoint hosted on AWS Elastic Beanstalk.

* **Live Endpoint:** `http://Ai-email-copilot-env.eba-qtnai9na.us-east-1.elasticbeanstalk.com/generate-email`

### Request Body (`POST`)
```json
{
  "sender_name": "Sparsh Gupta",
  "recipient_name": "HR Manager",
  "company_name": "ABC Technologies",
  "purpose": "Internship Request",
  "tone": "Professional",
  "length": "Medium",
  "key_points": ["Built RAG systems", "Strong in Python", "Passionate about AI"]
}
```

### Response Body
```json
{
  "success": true,
  "data": {
    "email": "Subject: Internship Inquiry - AI and Python Expertise\n\nDear HR Manager,\n\nI am writing to express my enthusiastic interest in internship opportunities at ABC Technologies..."
  }
}
```

---

## 🧪 Run Locally

### 1. Clone & Set Up Directory
```bash
git clone https://github.com/Sparsh2509/IBM_Project.git
cd IBM_Project
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY="your_google_gemini_api_key"
```

### 3. Run Streamlit UI Locally
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```
