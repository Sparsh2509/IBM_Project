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
    pdf.add_page()

    # Left & Right Margins
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)

    # Document Header Title
    pdf.set_font("helvetica", "B", 18)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 10, "PROJECT REPORT", ln=1, align="C")

    pdf.set_font("helvetica", "B", 14)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(
        0,
        8,
        "AI Email Copilot using Retrieval-Augmented Generation (RAG)",
        ln=1,
        align="C",
    )

    pdf.set_draw_color(200, 200, 200)
    pdf.set_line_width(0.5)
    pdf.line(20, pdf.get_y() + 2, 190, pdf.get_y() + 2)
    pdf.ln(8)

    # Metadata Block (Concept Note Style)
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(40, 6, "Application Name:")
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 6, "AI Email Copilot", ln=1)

    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(40, 6, "Domain:")
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 6, "Artificial Intelligence  |  Generative AI  |  Cloud Computing", ln=1)

    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(40, 6, "Submitted To:")
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 6, "IBM SkillsBuild / Project Evaluation Committee", ln=1)

    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(40, 6, "Prepared By:")
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 6, "Team GEN CREW (Unique ID: IBMBH00696)", ln=1)

    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(40, 6, "College Name:")
    pdf.set_font("helvetica", "", 10)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 6, "AJAY KUMAR GARG ENGINEERING COLLEGE", ln=1)
    pdf.ln(5)

    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(5)

    # 1. Project Title
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "1. Project Title", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6,
        "AI Email Copilot using Retrieval-Augmented Generation (RAG) and Google Gemini API.",
    )
    pdf.ln(4)

    # 2. Application Name
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "2. Application Name", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(0, 6, "AI Email Copilot")
    pdf.ln(4)

    # 3. Problem Statement
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "3. Problem Statement", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6,
        "Writing professional emails is time-consuming and challenging for students, job seekers, and fresh professionals. "
        "Most existing AI generation tools rely solely on generic prompt engineering, producing contextually shallow emails. "
        "Without an explicit retrieval grounding mechanism, the model lacks alignment with professional templates and standard communication norms. "
        "This project implements RAG to dynamically fetch relevant email template examples before prompting the generator, ensuring tone-perfect structure.",
    )
    pdf.ln(4)

    # 4. Project Objectives
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "4. Project Objectives", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6,
        "- Design and deploy an AI-powered web application that generates professional context-grounded emails.\n"
        "- Retrieve relevant email templates from a local vector store using Google gemini-embedding-2 API.\n"
        "- Leverage the Google Gemini 3.5 Flash LLM to produce structured, natural, and tone-accurate copy.\n"
        "- Decouple the setup into a REST API backend hosted on AWS Elastic Beanstalk and a Streamlit Cloud UI frontend.",
    )
    pdf.ln(4)

    # 5. Proposed Solution
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "5. Proposed Solution", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6,
        "- Uses Retrieval-Augmented Generation (RAG) to fetch matching sample categories (e.g. cold email, internship request, apology).\n"
        "- Employs Google's latest embedding model to encode documents and queries into 3072-dimensional space, removing local CPU/RAM overhead.\n"
        "- Saves and queries vector representations via a local FAISS database, achieving milliseconds similarity search.\n"
        "- Features a split frontend/backend setup: FastAPI running on AWS Elastic Beanstalk and Streamlit running on Streamlit Cloud.",
    )
    pdf.ln(4)

    # 6. Tech Stack
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "6. Technical Tech Stack", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6,
        "- Languages: Python 3.11\n"
        "- APIs used: Google Gemini Embeddings API (gemini-embedding-2), Gemini LLM API (gemini-3.5-flash)\n"
        "- RAG Frameworks: LangChain-Core, LangChain-Google-GenAI, FAISS-CPU\n"
        "- Backend Deployment: AWS Elastic Beanstalk (Amazon Linux 2023, Python 3.11 platform, t3.micro free-tier)\n"
        "- Frontend Deployment: Streamlit Cloud (Automatically updated via GitHub integration)\n"
        "- Utilities: python-dotenv, FastAPI, Uvicorn, Requests",
    )
    pdf.ln(4)

    # 7. Deployment Configuration & Resolution
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "7. Cloud Deployment & Fixes", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6,
        "- Out-Of-Memory (OOM) Fix: Replaced massive PyTorch sentence-transformers with Google's hosted embedding API, reducing startup RAM utilization to under 90MB on AWS.\n"
        "- Procfile formatting: Stripped CRLF carriage returns and trailing lines to ensure correct parsing by AWS Beanstalk platform engine.\n"
        "- Port settings: Configured Procfile to bind Uvicorn to port 8000 to match AWS EB default Nginx proxy routing rules.\n"
        "- Streamlit Secrets: Configured secrets fallback using st.secrets to seamlessly resolve dynamic API URLs in Streamlit Cloud environments.",
    )
    pdf.ln(4)

    # 8. Live Verification & Outputs
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "8. Live Verification & Links", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6,
        "The project has been fully deployed. Verification tests show code 200 success with zero latency issues.\n\n"
        "- Live UI Link: https://ibmproject-gruy5zavcwsnugwcwwx9js.streamlit.app/\n"
        "- Live Backend REST API Endpoint: http://Ai-email-copilot-env.eba-qtnai9na.us-east-1.elasticbeanstalk.com/generate-email\n"
        "- GitHub Repository: https://github.com/Sparsh2509/IBM_Project",
    )
    pdf.ln(4)

    # 9. Conclusion
    pdf.set_font("helvetica", "B", 12)
    pdf.set_text_color(33, 76, 121)
    pdf.cell(0, 8, "9. Conclusion", ln=1)
    pdf.set_font("helvetica", "", 10.5)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        6,
        "The AI Email Copilot project successfully leverages AWS cloud capabilities and Google Gemini models "
        "to deliver a decoupled, scalable, and memory-efficient RAG system. The solution runs seamlessly within the "
        "free-tier constraints of both AWS and Streamlit Cloud, achieving corporate template compliance and natural drafts.",
    )

    output_path = "Project_Report.pdf"
    pdf.output(output_path)
    print(f"Project Report PDF generated at: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    make_report()
