import os
from fpdf import FPDF


class ConceptReportPDF(FPDF):

    def header(self):
        self.set_font("helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
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
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()} of {{nb}}", border=0, align="C")


def make_report():
    pdf = ConceptReportPDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    # Left & Right Margins
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)

    # Cover Header
    pdf.set_font("helvetica", "B", 18)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 12, "PROJECT REPORT", ln=1, align="C")

    pdf.set_font("helvetica", "B", 13)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(
        0,
        8,
        "AI Email Copilot using Retrieval-Augmented Generation (RAG)",
        ln=1,
        align="C",
    )
    pdf.ln(5)

    pdf.set_draw_color(180, 180, 180)
    pdf.set_line_width(0.5)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(6)

    # Metadata (Concept Note Style)
    pdf.set_font("helvetica", "B", 10.5)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 6.5, "Application Name:")
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 6.5, "AI Email Copilot", ln=1)

    pdf.set_font("helvetica", "B", 10.5)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 6.5, "Domain:")
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 6.5, "Artificial Intelligence  |  Generative AI  |  Cloud Computing", ln=1)

    pdf.set_font("helvetica", "B", 10.5)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 6.5, "Submitted To:")
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 6.5, "IBM SkillsBuild / Project Evaluation Committee", ln=1)

    pdf.set_font("helvetica", "B", 10.5)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 6.5, "Prepared By:")
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 6.5, "Team GEN CREW (Unique ID: IBMBH00696)", ln=1)

    pdf.set_font("helvetica", "B", 10.5)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(45, 6.5, "College Name:")
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 6.5, "AJAY KUMAR GARG ENGINEERING COLLEGE", ln=1)
    pdf.ln(5)

    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(8)

    # 1. Project Title
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "1. Project Title", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 6, "AI Email Copilot using Retrieval-Augmented Generation (RAG)")
    pdf.ln(5)

    # 2. Application Name
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "2. Application Name", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(0, 6, "AI Email Copilot", ln=1)
    pdf.ln(5)

    # 3. Problem Statement
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "3. Problem Statement", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "- Writing professional emails is time-consuming and challenging for students, job seekers, and professionals.\n"
        "- Most existing AI tools rely only on prompt engineering, producing generic and contextually shallow emails.\n"
        "- No retrieval mechanism means the model lacks grounding in professional communication norms.\n"
        "- Users struggle with appropriate tone, structure, and personalization when composing formal emails.\n"
        "- This project solves the problem by using RAG to retrieve relevant examples before generation.",
    )
    pdf.ln(5)

    # 4. Project Objective
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "4. Project Objective", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "- Design and deploy an AI-powered web app that generates personalized, professional emails using RAG.\n"
        "- Retrieve semantically relevant email templates from a FAISS vector database using HuggingFace embeddings.\n"
        "- Use Google Gemini 2.5 Flash Lite as the LLM to produce structured, context-aware email content.\n"
        "- Demonstrate practical integration of LangChain, FAISS, HuggingFace, and Gemini in a production app.\n"
        "- Deploy the solution on AWS App Runner as a containerized, scalable cloud service using Docker.",
    )

    # Page 2
    pdf.add_page()
    # 5. Target Users
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "5. Target Users", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "Undergraduate and postgraduate students, job seekers and fresh graduates, working professionals, "
        "HR executives and recruiters, freelancers, and sales and business communication teams.",
    )
    pdf.ln(5)

    # 6. Proposed Solution
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "6. Proposed Solution", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "- Implements the Retrieval-Augmented Generation (RAG) architecture for grounded email generation.\n"
        "- Curated email templates (5 categories) are stored as dense vectors in a FAISS vector database.\n"
        "- User query is encoded using HuggingFace all-MiniLM-L6-v2 and matched against the index.\n"
        "- Top-K retrieved templates are injected into a structured LangChain prompt for Gemini 2.5 Flash Lite.\n"
        "- Streamlit provides the user-facing interface; FastAPI exposes a REST API for programmatic access.\n"
        "- Fully containerized with Docker and deployed on AWS App Runner for production-grade cloud hosting.",
    )
    pdf.ln(5)

    # 7. Key Features
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "7. Key Features", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "AI-powered professional email generation, RAG pipeline with FAISS semantic search, "
        "5 email purposes (cold email, internship, follow-up, apology, sales), "
        "5 communication tones + 3 length options, structured prompt engineering via LangChain, "
        "responsive Streamlit UI, FastAPI REST backend, secure API key management (.env / AWS env vars), "
        "Docker containerization, and AWS App Runner cloud deployment.",
    )

    # Page 3
    pdf.add_page()
    # 8. Technologies Used Table
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "8. Technologies Used", ln=1)
    pdf.ln(2)

    # Table Header
    pdf.set_fill_color(33, 76, 121)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 10.5)
    pdf.cell(80, 8, "Component", border=1, fill=True)
    pdf.cell(90, 8, "Technology", border=1, fill=True, ln=1)

    # Table Body
    table_data = [
        ("Programming Language", "Python 3.11"),
        ("Frontend / UI", "Streamlit"),
        ("Backend API", "FastAPI + Uvicorn"),
        ("AI Orchestration", "LangChain"),
        ("Large Language Model", "Google Gemini 2.5 Flash Lite"),
        ("Embedding Model", "HuggingFace all-MiniLM-L6-v2"),
        ("Vector Database", "FAISS (Facebook AI Similarity Search)"),
        ("Env Management", "python-dotenv"),
        ("Containerization", "Docker"),
        ("Cloud Deployment", "AWS App Runner"),
    ]

    pdf.set_text_color(60, 60, 60)
    pdf.set_font("helvetica", "", 10)
    for comp, tech in table_data:
        pdf.cell(80, 8, comp, border=1)
        pdf.cell(90, 8, tech, border=1, ln=1)
    pdf.ln(8)

    # 9. LLM Model Used
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "9. LLM Model Used", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "- Google Gemini 2.5 Flash Lite -- primary generative model; low-latency, high instruction-following capability.\n"
        "- Accessed via google-generativeai SDK and integrated through langchain-google-genai package.\n"
        "- Configured with temperature = 0.7 to balance creativity with coherent, structured output.\n"
        "- HuggingFace all-MiniLM-L6-v2 -- embedding model producing 384-dimensional sentence vectors.\n"
        "- Embeddings generated via HuggingFace Inference Endpoint API -- no local PyTorch download needed.\n"
        "- Embedding API choice reduces Docker image size significantly, improving cloud cold-start performance.",
    )

    # Page 4
    pdf.add_page()
    # 10. Application Workflow
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "10. Application Workflow", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)

    workflow_stages = [
        (
            "Stage 1 -- User Input",
            "User provides sender, recipient, company, purpose, tone, length, and key points via Streamlit UI.",
        ),
        (
            "Stage 2 -- Query Embedding",
            "Inputs combined into a semantic query string and encoded using HuggingFace all-MiniLM-L6-v2.",
        ),
        (
            "Stage 3 -- Semantic Search",
            "Encoded vector is matched against the FAISS index; top-K relevant email templates are retrieved.",
        ),
        (
            "Stage 4 -- Prompt Engineering",
            "Retrieved templates + user inputs assembled into a structured LangChain prompt with format rules.",
        ),
        (
            "Stage 5 -- Email Generation",
            "Prompt sent to Google Gemini 2.5 Flash Lite; model generates a complete, formatted email.",
        ),
        (
            "Stage 6 -- Output Delivery",
            "Final email with subject line, salutation, body, and closing displayed in the Streamlit interface.",
        ),
    ]

    for stage, desc in workflow_stages:
        pdf.set_font("helvetica", "B", 10.5)
        pdf.set_text_color(33, 76, 121)
        pdf.cell(0, 6, stage, ln=1)
        pdf.set_font("helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(0, 5.5, desc)
        pdf.ln(2)
    pdf.ln(3)

    # 11. Expected User Experience
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "11. Expected User Experience", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "- Clean, form-based Streamlit interface -- no technical knowledge required.\n"
        "- User fills sender/recipient/purpose/tone/length/key points and clicks Generate.\n"
        "- System retrieves templates and generates a complete, professional email within seconds.\n"
        "- Output includes subject line, salutation, structured body, and professional closing.\n"
        "- Generated email can be directly copied and sent with minimal or no editing.",
    )

    # Page 5
    pdf.add_page()
    # 12. Expected Outcomes
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "12. Expected Outcomes", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "- Significant reduction in time and effort required to compose professional emails.\n"
        "- Contextually accurate, well-structured emails matching purpose, tone, and user key points.\n"
        "- Practical demonstration of a full RAG pipeline using FAISS, HuggingFace, and Gemini.\n"
        "- Showcase of end-to-end MLOps: data prep -- model integration -- UI -- Docker -- cloud deployment.\n"
        "- Scalable, production-grade AI application deployed on AWS App Runner.",
    )
    pdf.ln(5)

    # 13. Innovation and Uniqueness
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "13. Innovation and Uniqueness", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "- Applies RAG to professional email generation -- a domain typically limited to prompt-only approaches.\n"
        "- Retrieval grounds the LLM output in real template examples, producing more contextually accurate emails.\n"
        "- Uses HuggingFace Inference Endpoint API instead of a local model -- reduces Docker image by ~2 GB.\n"
        "- Parallel REST API (FastAPI) alongside Streamlit UI demonstrates production-grade architecture.\n"
        "- Full containerization and AWS App Runner deployment distinguishes it from typical student AI projects.",
    )
    pdf.ln(5)

    # 14. Future Scope
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "14. Future Scope", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "- Expand the knowledge base with additional email categories (vendor, performance review, support).\n"
        "- Add user feedback loop to improve retrieval quality through reinforcement signals.\n"
        "- Introduce multi-language support for regional professional email generation.\n"
        "- Integrate Gmail / Outlook API for one-click email dispatch directly from the application.\n"
        "- Add user authentication, email history, and session management for personalized experience.",
    )
    pdf.ln(5)

    # 15. Conclusion
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "15. Conclusion", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6.2,
        "- AI Email Copilot demonstrates a practical, production-ready application of Retrieval-Augmented Generation.\n"
        "- Combines FAISS semantic search, HuggingFace embeddings, and Google Gemini 2.5 Flash Lite via LangChain.\n"
        "- Delivers context-aware, personalized email generation that surpasses prompt-only approaches in quality.\n"
        "- Meets industry standards: modular codebase, secure key management, Docker, and AWS cloud deployment.\n"
        "- Represents a holistic implementation of the modern AI development lifecycle from data to cloud.",
    )

    output_path = "Project_Report.pdf"
    pdf.output(output_path)
    print(f"Project Report PDF generated at: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    make_report()
