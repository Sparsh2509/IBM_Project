# PROJECT REPORT: AI EMAIL COPILOT
## AICTE | IBM SkillsBuild Gen AI & Cloud Computing Internship

---

### **Project Metadata**
* **Project Title:** AI Email Copilot (RAG-Powered Custom Email Generator)
* **Unique Team ID:** IBMBH00696
* **Team Name:** GEN CREW
* **Team Leader Name:** Sparsh Gupta
* **Total Team Members:** 5
* **College Name:** AJAY KUMAR GARG ENGINEERING COLLEGE
* **Live UI Link:** [https://ibmproject-gruy5zavcwsnugwcwwx9js.streamlit.app/](https://ibmproject-gruy5zavcwsnugwcwwx9js.streamlit.app/)
* **Live REST API Link:** [http://Ai-email-copilot-env.eba-qtnai9na.us-east-1.elasticbeanstalk.com](http://Ai-email-copilot-env.eba-qtnai9na.us-east-1.elasticbeanstalk.com)

---

## 1. Abstract
The **AI Email Copilot** is a state-of-the-art enterprise productivity tool designed to automate the creation of context-aware, highly personalized professional emails. Traditional LLM-based prompt generators often suffer from inconsistencies in tone, layout, and phrasing. To solve this, our project implements **Retrieval-Augmented Generation (RAG)** by coupling a fast local vector search engine (**FAISS**) with state-of-the-art Generative AI models from Google. 

The architecture is divided into a robust backend REST API hosted on **AWS Elastic Beanstalk (AL2023)** and an interactive frontend UI hosted on **Streamlit Cloud**. Through the use of Google's high-dimensional `gemini-embedding-2` model and the latest `gemini-3.5-flash` model, this project achieves high-speed processing, absolute deployment stability, and zero local memory footprint, making it fully eligible for free-tier cloud architectures.

---

## 2. Introduction & Objectives
Writing emails in professional, administrative, and corporate settings requires exact tones, appropriate context, and structured layouts. The objectives of this project are:
1. **Consistency:** Ensure generated emails adhere to vetted organizational templates.
2. **Context-Awareness:** Allow users to specify names, purposes, companies, and custom key points, which are automatically blended into the final output.
3. **Multi-Platform Deployment:** Build a production-grade decoupled system where the backend engine (FastAPI) and frontend (Streamlit) communicate securely over HTTP.
4. **Cloud-Native & Resource Optimized:** Deploy the backend on AWS Elastic Beanstalk using free-tier instances (t3.micro) with low CPU and memory footprints.

---

## 3. Solution Architecture & System Design
Our architecture is split into a **decidedly decoupled frontend-backend model** to ensure scalability and reliability:

### **Data Flow Architecture**
```
[User Input via Streamlit UI]
           │
           ▼ (HTTP POST /generate-email JSON Payload)
   [FastAPI Backend Server on AWS Elastic Beanstalk]
           │
           ├─► [Gemini Embeddings API (gemini-embedding-2)] ──► Convert query to 3072-D vector
           │
           ├─► [Local FAISS DB Vector Similarity Search] ──► Retrieve top relevant templates
           │
           └─► [Gemini 3.5 Flash LLM] ──► Generate final response with templates as context
           │
           ▼ (JSON HTTP Response)
[Streamlit UI displays generated output]
```

### **Core Components**
1. **Vectorization Engine (`rag/build_vectorstore.py`):** Loads sample email templates from the raw text directory, splits the documents into chunks, generates 3072-dimensional embeddings via Gemini API, and saves a local binary vector index using FAISS.
2. **Search & Retrieval (`rag/retriever.py`):** Runs online vector searches to fetch contextually similar email structures to guide the generator.
3. **Prompt Engineer (`prompts/email_prompt.py`):** Combines the retrieved templates, user-provided sender/recipient details, tone constraints, length specifications, and custom bullet points into a structured system instruction prompt.
4. **REST Web Server (`api.py`):** A FastAPI wrapper running on Uvicorn that exposes the entire pipeline over a public POST API endpoint.
5. **Interactive UI Client (`streamlit_app.py`):** A web-based application utilizing Streamlit to gather user inputs and interact with the live AWS backend.

---

## 4. Technical Specifications & Cloud Infrastructure

* **Programming Language:** Python 3.11
* **Backend Framework:** FastAPI, Uvicorn (WSGI/ASGI runner)
* **Frontend Framework:** Streamlit
* **RAG Orchestrator:** LangChain (LangChain-Community, LangChain-Core)
* **Vector Store:** FAISS (CPU variant)
* **Embedding Model:** Google Generative AI Embeddings (`gemini-embedding-2`)
* **Generation Model:** Google Gemini (`gemini-3.5-flash`)
* **Backend Cloud Host:** AWS Elastic Beanstalk (Running Python 3.11 on 64-bit Amazon Linux 2023, t3.micro instance)
* **Frontend Cloud Host:** Streamlit Cloud (Auto-syncing from GitHub repository)

---

## 5. Implementation Challenges & Resolutions
During the development and cloud deployment lifecycle, the team encountered several major engineering roadblocks which were successfully resolved:

1. **Memory Exhaustion (OOM) on AWS t3.micro Free Tier:**
   * *Problem:* Initially, PyTorch and Hugging Face's local `sentence-transformers` were used for embeddings. This resulted in an enormous memory footprint (>1.2 GB RAM) during builds/runtime, immediately causing the 1GB RAM t3.micro instance on AWS to freeze and crash.
   * *Resolution:* Migrated from local PyTorch embeddings to Google's cloud-hosted **`gemini-embedding-2`** API. This eliminated the PyTorch and local model dependencies entirely, reducing memory utilization by over 90% and speeding up index load times to milliseconds.
2. **Windows vs. Linux ZIP Packaging Mismatch:**
   * *Problem:* Standard Windows zip utilities create paths with backslashes (`\`), which cause unzip extraction failures on the Amazon Linux platform during deployment.
   * *Resolution:* Used `git archive` to package code, ensuring Unix-compatible forward-slash (`/`) directory paths.
3. **AWS Elastic Beanstalk Procfile Parsing Failure:**
   * *Problem:* Procfiles created on Windows contain CRLF (`\r\n`) endings and trailing empty lines which break the Beanstalk process manager engine during environment startup.
   * *Resolution:* Re-wrote the Procfile natively with exactly one line using binary Unix LF (`\n`) encoding.
4. **Streamlit Cloud Environment Secrets Fetching:**
   * *Problem:* Streamlit Cloud does not automatically bind TOML secrets to environment variables accessed via `os.getenv`.
   * *Resolution:* Updated code to dynamically query `st.secrets.get()` as a fallback configuration for `API_URL` and `GEMINI_API_KEY`.

---

## 6. Verification & Test Case Outputs
Below is a verification test run executed against the live **AWS Elastic Beanstalk REST API**:

### **HTTP POST Payload Sent:**
```json
{
  "sender_name": "Sparsh",
  "recipient_name": "Harsh",
  "company_name": "IBM",
  "purpose": "follow up",
  "tone": "professional",
  "length": "short",
  "key_points": ["Hi", "Checking in on the project status"]
}
```

### **REST API Status Return:**
`200 OK`

### **Generated Email Output Received:**
```text
Subject: Follow-Up: Project Status

Dear Harsh,

I hope you are having a productive week. I am writing to check in on our project's status and see if there are any updates from your side. Please let me know if you need any additional information or support from my end to help move things forward.

Best regards,
Sparsh
```

---

## 7. Conclusion & Future Enhancements
The **AI Email Copilot** successfully demonstrates how RAG architectures can optimize prompt engineering for professional communications. By moving memory-intensive vectorization and generation tasks to secure cloud APIs, and keeping deployment configurations clean, the project achieves production-grade efficiency entirely on a zero-cost budget.

### **Future Roadmap:**
* **Multimodal Inputs:** Expanding RAG to support parsing PDF/Doc attachment prompts using Gemini multimodal architectures.
* **Auto-drafting Extensions:** Building chrome/outlook extensions that hook the FastAPI REST API directly into GMail and Outlook mail composers.
* **User Feedback Loops:** Logging generated email modifications to continuously fine-tune similarity scores in the FAISS vector database.
