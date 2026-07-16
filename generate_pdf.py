import os
from fpdf import FPDF


class NormalPDFReport(FPDF):

    def header(self):
        self.set_font("helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(
            0,
            10,
            "PROJECT REPORT  |  AI Email Copilot  |  Team GEN CREW",
            border=0,
            ln=1,
            align="R",
        )
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()} of {{nb}}", border=0, align="C")


def make_report():
    pdf = NormalPDFReport()
    pdf.alias_nb_pages()

    # Margin settings
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)

    # ------------------ PAGE 1: TITLE PAGE ------------------
    pdf.add_page()
    pdf.ln(20)
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 15, "PROJECT REPORT", ln=1, align="C")
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(
        0,
        8,
        "AI Email Copilot using Retrieval-Augmented Generation (RAG)",
        ln=1,
        align="C",
    )

    pdf.set_draw_color(33, 76, 121)
    pdf.set_line_width(1.0)
    pdf.line(20, pdf.get_y() + 5, 190, pdf.get_y() + 5)
    pdf.ln(20)

    # Metadata Block
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 8, "Application Name:")
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 8, "AI Email Copilot", ln=1)

    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 8, "Domain:")
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 8, "Artificial Intelligence  |  Generative AI  |  Cloud Computing", ln=1)

    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 8, "Submitted To:")
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 8, "IBM SkillsBuild / Project Evaluation Committee", ln=1)

    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 8, "Prepared By:")
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 8, "Team GEN CREW (Unique ID: IBMBH00696)", ln=1)

    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 8, "College Name:")
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(0, 8, "AJAY KUMAR GARG ENGINEERING COLLEGE")
    
    pdf.set_font("helvetica", "B", 11)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 8, "Submission Date:")
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 8, "July 2026", ln=1)
    pdf.ln(10)

    pdf.set_draw_color(200, 200, 200)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(15)

    pdf.set_font("helvetica", "I", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 6, "Note: This document constitutes the final technical deliverable report detailing system design, local RAG architectures, model selection, code implementation, and cloud deployment procedures on AWS Elastic Beanstalk.")

    # ------------------ PAGE 2: ABSTRACT & INTRODUCTION ------------------
    pdf.add_page()
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "1. Executive Summary & Abstract", ln=1)
    pdf.set_draw_color(33, 76, 121)
    pdf.set_line_width(0.5)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(
        0,
        6,
        "The AI Email Copilot is a production-grade enterprise application built to optimize corporate and administrative email communications. While common Large Language Models (LLMs) can generate text in response to simple prompts, they frequently exhibit formatting drift, hallucinated templates, and lack contextual grounding in specific domain norms.\n\n"
        "To address this bottleneck, our system implements a hybrid Retrieval-Augmented Generation (RAG) pattern. It stores a vetted collection of standard email templates in a local FAISS vector database. When a user creates a generation query, the system retrieves the most contextually relevant templates using high-speed cosine vector match, injects the examples directly into a prompt template, and invokes the latest Google Gemini LLM API.\n\n"
        "The complete system is decoupled into a backend FastAPI REST server deployed on AWS Elastic Beanstalk (Amazon Linux 2023, t3.micro) and an interactive frontend UI hosted on Streamlit Cloud, achieving high scalability and memory optimizations.",
    )
    pdf.ln(5)

    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "2. Introduction", ln=1)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.multi_cell(
        0,
        6,
        "In modern education and corporate settings, drafting effective professional emails (e.g. cold outreach, follow ups, and internship applications) is vital. However, many users struggle with formatting, appropriate language levels, and structural alignments.\n\n"
        "This project outlines a scalable design to generate localized custom professional emails on demand. Key features include user-defined sender/recipient parameters, company contexts, customizable key bullet points, custom tone parameters, and text length limits. The design leverages Google's serverless embedding architectures to construct vector spaces at zero runtime memory overhead.",
    )

    # ------------------ PAGE 3: PROBLEM STATEMENT & OBJECTIVES ------------------
    pdf.add_page()
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "3. Problem Statement", ln=1)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.multi_cell(
        0,
        6,
        "The primary difficulties in automating professional email communications are as follows:\n\n"
        "- Generic LLM Responses: Standard prompt-based generators lack specialized organizational context, leading to repetitive or shallow email copy.\n"
        "- Inconsistent Styling: LLMs are prone to structural drifts, occasionally omitting necessary elements like subject lines or formal signatures.\n"
        "- High Memory Requirements: Conventional RAG pipelines running local open-source transformer models require substantial local RAM (typically >1GB), making deployment on lightweight free-tier cloud servers impossible.\n"
        "- Deployment Failures: Many cloud services fail to host heavy containerized environments due to strict memory limit constraints.",
    )
    pdf.ln(10)

    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "4. Project Objectives", ln=1)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.multi_cell(
        0,
        6,
        "The key objectives driving the engineering lifecycle of this system include:\n\n"
        "1. Context Grounding: Build a retrieval mechanism that forces the LLM generator to align with pre-approved corporate layouts.\n"
        "2. API Decoupling: Architect a public REST endpoint using FastAPI to handle vector database search and generation logic independently of the client interface.\n"
        "3. Performance Optimizations: Structure memory-efficient configurations to run the complete FastAPI application in cloud environments using less than 100MB RAM.\n"
        "4. Seamless UI Connection: Bind the frontend Streamlit application dynamically to the cloud REST service via secure HTTP requests.",
    )

    # ------------------ PAGE 4: SYSTEM DESIGN & ADVANTAGES ------------------
    pdf.add_page()
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "5. RAG System Design & Advantages", ln=1)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.multi_cell(
        0,
        6,
        "Instead of fine-tuning the model or relying on plain prompts, our project implements Retrieval-Augmented Generation (RAG). "
        "The RAG design brings distinct advantages:\n\n"
        "A. Reduced Hallucination:\n"
        "By injecting real templates as a reference context, the LLM generates drafts closely matching verified business communication standards.\n\n"
        "B. Easy Knowledge Updates:\n"
        "Vetted email templates can be added or modified instantly in the text directory. The system simply rebuilds the vector index without requiring expensive retraining or fine-tuning cycles.\n\n"
        "C. Dense Vector Representation:\n"
        "Using Google's gemini-embedding-2 API, the documents are transformed into dense 3072-dimensional floating-point vectors, capturing detailed semantics for accurate template matching.\n\n"
        "D. Efficient Vector Space:\n"
        "The FAISS database handles fast similarity calculations locally, scanning vectors in microseconds.",
    )
    pdf.ln(10)

    # ------------------ PAGE 5: BACKEND ENGINE CODE ------------------
    pdf.add_page()
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "6. Backend Implementation & Vector Search", ln=1)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.multi_cell(
        0,
        6,
        "The backend is written in FastAPI and uses LangChain to connect FAISS with the Gemini model. "
        "Below is the core implementation of the retriever module (rag/retriever.py):",
    )
    pdf.ln(2)

    pdf.set_fill_color(245, 247, 250)
    pdf.set_font("courier", "", 9)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(
        0,
        5.5,
        "import os\n"
        "from langchain_google_genai import GoogleGenerativeAIEmbeddings\n"
        "from langchain_community.vectorstores import FAISS\n\n"
        "load_dotenv()\n\n"
        "# Load embedding model\n"
        "embeddings = GoogleGenerativeAIEmbeddings(\n"
        "    model='models/gemini-embedding-2',\n"
        "    google_api_key=os.getenv('GEMINI_API_KEY')\n"
        ")\n\n"
        "# Load FAISS vector database index\n"
        "vectorstore = FAISS.load_local(\n"
        "    'faiss_index',\n"
        "    embeddings,\n"
        "    allow_dangerous_deserialization=True\n"
        ")\n\n"
        "retriever = vectorstore.as_retriever(search_kwargs={'k': 2})\n\n"
        "def retrieve_context(query: str) -> str:\n"
        "    docs = retriever.invoke(query)\n"
        "    return '\\n\\n'.join([doc.page_content for doc in docs])",
        border=1,
        fill=True,
    )

    # ------------------ PAGE 6: FRONTEND STREAMLIT DESIGN ------------------
    pdf.add_page()
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "7. Frontend UI Design & Flow", ln=1)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(
        0,
        6,
        "The frontend is implemented in streamlit_app.py. It provides a simple, clean form interface to collect user inputs. "
        "Instead of direct function calls, the UI calls the backend REST API over HTTP, allowing total decoupling.\n\n"
        "Below is a code listing showing how Streamlit handles API communication:",
    )
    pdf.ln(2)

    pdf.set_fill_color(245, 247, 250)
    pdf.set_font("courier", "", 9)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(
        0,
        5.5,
        "import streamlit as st\n"
        "import requests\n"
        "import os\n\n"
        "# Resolve backend URL using env var or Streamlit Cloud Secrets\n"
        "API_URL = os.getenv('API_URL') or st.secrets.get('API_URL') or 'http://localhost:8000'\n\n"
        "with st.form('email_form'):\n"
        "    sender = st.text_input('Sender Name')\n"
        "    recipient = st.text_input('Recipient Name')\n"
        "    purpose = st.selectbox('Purpose', ['cold email', 'internship request'])\n"
        "    key_points = st.text_area('Key Points')\n"
        "    submit = st.form_submit_button('Generate Email')\n\n"
        "if submit:\n"
        "    response = requests.post(\n"
        "        f'{API_URL}/generate-email',\n"
        "        json={\n"
        "            'sender_name': sender,\n"
        "            'recipient_name': recipient,\n"
        "            'key_points': key_points.split('\\n')\n"
        "            # other inputs...\n"
        "        }\n"
        "    )\n"
        "    st.write(response.json()['data']['email'])",
        border=1,
        fill=True,
    )

    # ------------------ PAGE 7: CLOUD DEPLOYMENT Lifecycle ------------------
    pdf.add_page()
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "8. AWS Elastic Beanstalk Deployment", ln=1)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(
        0,
        6,
        "The backend API is hosted on AWS Elastic Beanstalk using Python 3.11 running on 64-bit Amazon Linux 2023. "
        "The deployment process handles dependency installation and process management automatically.\n\n"
        "A. Requirements Merging:\n"
        "To ensure all FastAPI and LangChain packages are installed during startup, we merged backend dependencies into "
        "requirements.txt. This allows AWS EB to install libraries in the virtual environment natively.\n\n"
        "B. Nginx Proxy Configuration:\n"
        "AWS Elastic Beanstalk sets up an Nginx reverse proxy server by default. We bound Uvicorn to run on port 8000 "
        "via our Procfile to perfectly match the Nginx default proxy target.\n\n"
        "C. Procfile Structure:\n"
        "Our Procfile specifies the WSGI process startup command and uses a single Unix-native newline (LF) to prevent platform extraction failures:",
    )
    pdf.ln(2)

    pdf.set_fill_color(245, 247, 250)
    pdf.set_font("courier", "", 10)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(
        0,
        6,
        "web: uvicorn api:app --host 0.0.0.0 --port 8000",
        border=1,
        fill=True,
    )

    # ------------------ PAGE 8: SCREENSHOT 1 ------------------
    pdf.add_page()
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "9. Streamlit User Interface - Input Form", ln=1)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(
        0,
        6,
        "Below is a screenshot of the active user interface hosted on Streamlit Cloud. It provides fields "
        "to specify email metadata (Sender, Recipient, Company, Purpose, Tone, Length, and Key Points).",
    )
    pdf.ln(5)

    # Embed input screenshot
    screenshot_input = "ui_screenshot_input.png"
    if os.path.exists(screenshot_input):
        pdf.image(screenshot_input, x=20, w=170)
    else:
        pdf.cell(0, 10, "[Streamlit UI Input Form Screenshot]", border=1, ln=1, align="C")

    # ------------------ PAGE 9: SCREENSHOT 2 ------------------
    pdf.add_page()
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "10. Streamlit User Interface - Generated Output", ln=1)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(
        0,
        6,
        "Below is a screenshot showing the successfully generated email copy retrieved using our RAG pipeline "
        "and formatted by the Google Gemini 3.5 Flash LLM on AWS.",
    )
    pdf.ln(5)

    # Embed output screenshot
    screenshot_output = "ui_screenshot_output.png"
    if os.path.exists(screenshot_output):
        pdf.image(screenshot_output, x=20, w=170)
    else:
        pdf.cell(0, 10, "[Streamlit UI Generated Output Screenshot]", border=1, ln=1, align="C")

    # ------------------ PAGE 10: CONCLUSION & SECURITY ------------------
    pdf.add_page()
    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "11. Security, Scaling & Conclusion", ln=1)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(
        0,
        6,
        "A. Secrets and Security Management:\n"
        "API keys are loaded securely as AWS Elastic Beanstalk environment variables, preventing sensitive tokens "
        "from leaking in source code. On Streamlit Cloud, keys are bound securely in the encrypted secrets dashboard.\n\n"
        "B. Scaling and Load Optimization:\n"
        "By utilizing serverless endpoints for both model embeddings and generation text, the AWS backend instance "
        "is only responsible for handling HTTP routing and FAISS index similarity scans. This architecture "
        "allows the application to scale efficiently without rising CPU/RAM usage.\n\n"
        "C. Final Conclusion:\n"
        "The AI Email Copilot successfully delivers a production-grade, decoupled cloud application. By coupling "
        "local vector databases with hosted LLMs, the system achieves RAG-grounded formatting accuracy, "
        "establishing a stable template generator tool for AICTE | IBM project submission guidelines.",
    )

    output_path = "Project_Report.pdf"
    pdf.output(output_path)
    print(f"Project Report PDF generated at: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    make_report()
