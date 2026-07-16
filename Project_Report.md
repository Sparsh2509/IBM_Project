# PROJECT REPORT: AI EMAIL COPILOT
## AICTE | IBM SkillsBuild Gen AI & Cloud Computing Internship

---

### **Project Metadata**
* **Application Name:** AI Email Copilot
* **Domain:** Artificial Intelligence | Generative AI | Cloud Computing
* **Submitted To:** IBM SkillsBuild / Project Evaluation Committee
* **Prepared By:** Team GEN CREW (Unique ID: IBMBH00696)
* **College Name:** AJAY KUMAR GARG ENGINEERING COLLEGE
* **Submission Date:** July 2026
* **Live UI Link:** [https://ibmproject-gruy5zavcwsnugwcwwx9js.streamlit.app/](https://ibmproject-gruy5zavcwsnugwcwwx9js.streamlit.app/)
* **Live REST API Link:** [http://Ai-email-copilot-env.eba-qtnai9na.us-east-1.elasticbeanstalk.com](http://Ai-email-copilot-env.eba-qtnai9na.us-east-1.elasticbeanstalk.com)

---

## 1. Executive Summary & Abstract
The AI Email Copilot is a production-grade enterprise application built to optimize corporate and administrative email communications. While common Large Language Models (LLMs) can generate text in response to simple prompts, they frequently exhibit formatting drift, hallucinated templates, and lack contextual grounding in specific domain norms.

To address this bottleneck, our system implements a hybrid Retrieval-Augmented Generation (RAG) pattern. It stores a vetted collection of standard email templates in a local FAISS vector database. When a user creates a generation query, the system retrieves the most contextually relevant templates using high-speed cosine vector match, injects the examples directly into a prompt template, and invokes the latest Google Gemini LLM API.

The complete system is decoupled into a backend FastAPI REST server deployed on AWS Elastic Beanstalk (Amazon Linux 2023, t3.micro) and an interactive frontend UI hosted on Streamlit Cloud, achieving high scalability and memory optimizations.

---

## 2. Introduction
In modern education and corporate settings, drafting effective professional emails (e.g. cold outreach, follow ups, and internship applications) is vital. However, many users struggle with formatting, appropriate language levels, and structural alignments.

This project outlines a scalable design to generate localized custom professional emails on demand. Key features include user-defined sender/recipient parameters, company contexts, customizable key bullet points, custom tone parameters, and text length limits. The design leverages Google's serverless embedding architectures to construct vector spaces at zero runtime memory overhead.

---

## 3. Problem Statement
The primary difficulties in automating professional email communications are as follows:
* **Generic LLM Responses:** Standard prompt-based generators lack specialized organizational context, leading to repetitive or shallow email copy.
* **Inconsistent Styling:** LLMs are prone to structural drifts, occasionally omitting necessary elements like subject lines or formal signatures.
* **High Memory Requirements:** Conventional RAG pipelines running local open-source transformer models require substantial local RAM (typically >1GB), making deployment on lightweight free-tier cloud servers impossible.
* **Deployment Failures:** Many cloud services fail to host heavy containerized environments due to strict memory limit constraints.

---

## 4. Project Objectives
The key objectives driving the engineering lifecycle of this system include:
1. **Context Grounding:** Build a retrieval mechanism that forces the LLM generator to align with pre-approved corporate layouts.
2. **API Decoupling:** Architect a public REST endpoint using FastAPI to handle vector database search and generation logic independently of the client interface.
3. **Performance Optimizations:** Structure memory-efficient configurations to run the complete FastAPI application in cloud environments using less than 100MB RAM.
4. **Seamless UI Connection:** Bind the frontend Streamlit application dynamically to the cloud REST service via secure HTTP requests.

---

## 5. RAG System Design & Advantages
Instead of fine-tuning the model or relying on plain prompts, our project implements Retrieval-Augmented Generation (RAG). The RAG design brings distinct advantages:

### **A. Reduced Hallucination**
By injecting real templates as a reference context, the LLM generates drafts closely matching verified business communication standards.

### **B. Easy Knowledge Updates**
Vetted email templates can be added or modified instantly in the text directory. The system simply rebuilds the vector index without requiring expensive retraining or fine-tuning cycles.

### **C. Dense Vector Representation**
Using Google's `gemini-embedding-2` API, the documents are transformed into dense 3072-dimensional floating-point vectors, capturing detailed semantics for accurate template matching.

### **D. Efficient Vector Space**
The FAISS database handles fast similarity calculations locally, scanning vectors in microseconds.

---

## 6. Backend Implementation & Vector Search
The backend is written in FastAPI and uses LangChain to connect FAISS with the Gemini model. Below is the core implementation of the retriever module (`rag/retriever.py`):

```python
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

# Load embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model='models/gemini-embedding-2',
    google_api_key=os.getenv('GEMINI_API_KEY')
)

# Load FAISS vector database index
vectorstore = FAISS.load_local(
    'faiss_index',
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={'k': 2})

def retrieve_context(query: str) -> str:
    docs = retriever.invoke(query)
    return '\n\n'.join([doc.page_content for doc in docs])
```

---

## 7. Frontend UI Design & Flow
The frontend is implemented in `streamlit_app.py`. It provides a simple, clean form interface to collect user inputs. Instead of direct function calls, the UI calls the backend REST API over HTTP, allowing total decoupling.

Below is a code listing showing how Streamlit handles API communication:

```python
import streamlit as st
import requests
import os

# Resolve backend URL using env var or Streamlit Cloud Secrets
API_URL = os.getenv('API_URL') or st.secrets.get('API_URL') or 'http://localhost:8000'

with st.form('email_form'):
    sender = st.text_input('Sender Name')
    recipient = st.text_input('Recipient Name')
    purpose = st.selectbox('Purpose', ['cold email', 'internship request'])
    key_points = st.text_area('Key Points')
    submit = st.form_submit_button('Generate Email')

if submit:
    response = requests.post(
        f'{API_URL}/generate-email',
        json={
            'sender_name': sender,
            'recipient_name': recipient,
            'key_points': key_points.split('\n')
            # other inputs...
        }
    )
    st.write(response.json()['data']['email'])
```

---

## 8. AWS Elastic Beanstalk Deployment
The backend API is hosted on AWS Elastic Beanstalk using Python 3.11 running on 64-bit Amazon Linux 2023. The deployment process handles dependency installation and process management automatically.

* **Requirements Merging:** To ensure all FastAPI and LangChain packages are installed during startup, we merged backend dependencies into `requirements.txt`. This allows AWS EB to install libraries in the virtual environment natively.
* **Nginx Proxy Configuration:** AWS Elastic Beanstalk sets up an Nginx reverse proxy server by default. We bound Uvicorn to run on port 8000 via our Procfile to perfectly match the Nginx default proxy routing rules.
* **Procfile Structure:** Our Procfile specifies the WSGI process startup command and uses a single Unix-native newline (LF) to prevent platform extraction failures:
  ```text
  web: uvicorn api:app --host 0.0.0.0 --port 8000
  ```

---

## 9. Streamlit User Interface screenshots
The active user interface screenshots hosted on Streamlit Cloud are compiled in the PDF version of this report. 

* **Input Page:** Captures email metadata (Sender, Recipient, Company, Purpose, Tone, Length, and Key Points).
* **Output Page:** Renders the contextually matched retrieved text structured and generated via Google Gemini 3.5 Flash.

---

## 10. Security, Scaling & Conclusion

### **A. Secrets and Security Management**
API keys are loaded securely as AWS Elastic Beanstalk environment variables, preventing sensitive tokens from leaking in source code. On Streamlit Cloud, keys are bound securely in the encrypted secrets dashboard.

### **B. Scaling and Load Optimization**
By utilizing serverless endpoints for both model embeddings and generation text, the AWS backend instance is only responsible for handling HTTP routing and FAISS index similarity scans. This architecture allows the application to scale efficiently without rising CPU/RAM usage.

### **C. Final Conclusion**
The AI Email Copilot project successfully delivers a production-grade, decoupled cloud application. By coupling local vector databases with hosted LLMs, the system achieves RAG-grounded formatting accuracy, establishing a stable template generator tool for AICTE | IBM project submission guidelines.
