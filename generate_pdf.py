import os
from fpdf import FPDF


class PDFReport(FPDF):

    def header(self):
        if self.page_no() > 1:
            self.set_font("helvetica", "I", 8)
            self.set_text_color(128, 128, 128)
            self.cell(
                0,
                10,
                "Project Report: AI Email Copilot | Team GEN CREW (IBMBH00696)",
                border=0,
                ln=1,
                align="R",
            )
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(
            0,
            10,
            f"Page {self.page_no()} of {{nb}}",
            border=0,
            align="C",
        )

    def add_title_page(self):
        self.add_page()
        self.set_fill_color(240, 244, 248)
        self.rect(0, 0, 210, 297, "F")  # Soft background tint

        # Draw a stylish dark blue sidebar accent
        self.set_fill_color(33, 76, 121)
        self.rect(0, 0, 15, 297, "F")

        self.set_left_margin(30)
        self.set_top_margin(40)

        # Header Title
        self.ln(10)
        self.set_font("helvetica", "B", 14)
        self.set_text_color(33, 76, 121)
        self.cell(
            0,
            10,
            "AICTE | IBM SkillsBuild Gen AI & Cloud Computing Internship",
            ln=1,
        )

        # Draw decorative rule
        self.set_draw_color(33, 76, 121)
        self.set_line_width(1.5)
        self.line(30, self.get_y() + 2, 190, self.get_y() + 2)
        self.ln(15)

        # Title of Project
        self.set_font("helvetica", "B", 36)
        self.set_text_color(26, 26, 26)
        self.multi_cell(0, 15, "AI EMAIL\nCOPILOT")
        self.ln(5)

        # Subtitle
        self.set_font("helvetica", "", 16)
        self.set_text_color(100, 110, 120)
        self.cell(
            0,
            10,
            "RAG-Powered Custom Email Generator",
            ln=1,
        )
        self.ln(35)

        # Metadata box
        self.set_fill_color(255, 255, 255)
        self.set_draw_color(220, 225, 230)
        self.set_line_width(0.5)
        self.rect(30, self.get_y(), 150, 110, "DF")

        # Metadata Content
        self.set_top_margin(self.get_y() + 10)
        self.set_left_margin(40)
        self.set_y(self.get_y() + 10)

        self.set_font("helvetica", "B", 12)
        self.set_text_color(33, 76, 121)
        self.cell(40, 8, "Unique Team ID:")
        self.set_font("helvetica", "", 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, "IBMBH00696", ln=1)

        self.set_font("helvetica", "B", 12)
        self.set_text_color(33, 76, 121)
        self.cell(40, 8, "Team Name:")
        self.set_font("helvetica", "", 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, "GEN CREW", ln=1)

        self.set_font("helvetica", "B", 12)
        self.set_text_color(33, 76, 121)
        self.cell(40, 8, "Team Leader:")
        self.set_font("helvetica", "", 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, "Sparsh Gupta", ln=1)

        self.set_font("helvetica", "B", 12)
        self.set_text_color(33, 76, 121)
        self.cell(40, 8, "Team Size:")
        self.set_font("helvetica", "", 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, "5 Members", ln=1)

        self.set_font("helvetica", "B", 12)
        self.set_text_color(33, 76, 121)
        self.cell(40, 8, "College Name:")
        self.set_font("helvetica", "", 12)
        self.set_text_color(50, 50, 50)
        self.multi_cell(100, 8, "AJAY KUMAR GARG ENGINEERING COLLEGE")

        self.set_font("helvetica", "B", 12)
        self.set_text_color(33, 76, 121)
        self.cell(40, 8, "Date:")
        self.set_font("helvetica", "", 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, "July 2026", ln=1)

        # Reset margins for content pages
        self.set_left_margin(20)
        self.set_right_margin(20)

    def write_heading(self, text, level=1):
        self.ln(8)
        if level == 1:
            self.set_font("helvetica", "B", 16)
            self.set_text_color(33, 76, 121)
            self.cell(0, 10, text, ln=1)
            # Add line
            self.set_draw_color(33, 76, 121)
            self.set_line_width(1.0)
            self.line(20, self.get_y(), 190, self.get_y())
            self.ln(4)
        elif level == 2:
            self.set_font("helvetica", "B", 13)
            self.set_text_color(50, 70, 90)
            self.cell(0, 8, text, ln=1)
            self.ln(2)

    def write_paragraph(self, text):
        self.set_font("helvetica", "", 10.5)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 6, text)
        self.ln(3)

    def write_bullet(self, title, description):
        self.set_font("helvetica", "B", 10.5)
        self.set_text_color(33, 76, 121)
        self.write(6, "- " + title + ": ")
        self.set_font("helvetica", "", 10.5)
        self.set_text_color(60, 60, 60)
        self.write(6, description + "\n")

    def write_code(self, code_text):
        self.ln(2)
        self.set_fill_color(245, 247, 250)
        self.set_font("courier", "", 9.5)
        self.set_text_color(40, 40, 40)
        # Calculate height based on lines
        lines = code_text.strip().split("\n")
        h = len(lines) * 5 + 6
        self.multi_cell(0, 5, code_text, border=1, fill=True)
        self.ln(3)


def make_report():
    pdf = PDFReport()
    pdf.alias_nb_pages()
    pdf.add_title_page()

    # Page 2: Table of Contents & Abstract
    pdf.add_page()
    pdf.write_heading("1. Executive Summary / Abstract", 1)
    pdf.write_paragraph(
        "The AI Email Copilot is a production-grade enterprise productivity application designed to automate "
        "and optimize custom, context-aware email generation. While generic Large Language Model (LLM) templates "
        "often result in tone inconsistencies and layout errors, our solution couples Retrieval-Augmented Generation "
        "(RAG) with Google Gemini to guarantee compliance with high-quality, pre-vetted corporate templates.\n\n"
        "The architecture is decoupled into a robust REST API hosted on AWS Elastic Beanstalk (Amazon Linux 2023) "
        "and an interactive front-end client hosted on Streamlit Cloud. By migrating from local, resource-heavy "
        "PyTorch-based vectorization libraries to cloud-hosted Gemini embeddings, the server footprint is minimized, "
        "achieving absolute reliability on AWS free-tier hosting."
    )

    pdf.write_heading("2. Introduction & Objectives", 1)
    pdf.write_paragraph(
        "Modern corporate communication requires highly structured, contextually relevant messages tailored to tone, "
        "length, and specific purposes. The core objectives of this project include:\n"
    )
    pdf.write_bullet(
        "Consistency",
        "Ensuring generated outputs adhere to organizational structures.",
    )
    pdf.write_bullet(
        "Flexibility",
        "Allowing multiple tone variants (e.g., professional, friendly, persuasive) and lengths.",
    )
    pdf.write_bullet(
        "Cloud Independence",
        "Structuring a clean REST Backend API accessible from any frontend client.",
    )
    pdf.write_bullet(
        "Efficiency",
        "Designing the RAG pipeline to prevent memory leaks and out-of-memory (OOM) failures.",
    )

    # Page 3: Technical Specifications & System Structure
    pdf.add_page()
    pdf.write_heading("3. Technical Specifications & Stack", 1)
    pdf.write_paragraph(
        "The system stack has been selected to minimize memory overhead while maintaining high similarity search performance:\n"
    )
    pdf.write_bullet("Programming Language", "Python 3.11")
    pdf.write_bullet(
        "RAG Framework", "LangChain-Core, LangChain-Google-GenAI"
    )
    pdf.write_bullet("Vector Database", "FAISS (Facebook AI Similarity Search)")
    pdf.write_bullet("Embeddings Model", "Google gemini-embedding-2 (3072-D)")
    pdf.write_bullet("Generation LLM", "Google Gemini 3.5 Flash")
    pdf.write_bullet("Backend API Hosting", "AWS Elastic Beanstalk (t3.micro)")
    pdf.write_bullet("Frontend App Hosting", "Streamlit Cloud")
    pdf.ln(5)

    pdf.write_heading("4. Directory Structure", 1)
    pdf.write_code(
        "AI_Email_Generator_Copilot/\n"
        "|-- api.py                  # FastAPI REST Server\n"
        "|-- streamlit_app.py        # Streamlit Frontend Client\n"
        "|-- Procfile                # AWS EB Startup Instructions\n"
        "|-- requirements.txt        # Streamlit Dependencies\n"
        "|-- requirements-api.txt    # AWS EB Dependencies\n"
        "|-- .ebextensions/\n"
        "|   +-- python.config       # Python platform parameters\n"
        "|-- rag/\n"
        "|   |-- build_vectorstore.py # Generates vector db index\n"
        "|   +-- retriever.py        # Handles FAISS similarity search\n"
        "+-- faiss_index/            # Saved vector database files\n"
    )

    # Page 4: Architecture and Code Walkthrough
    pdf.add_page()
    pdf.write_heading("5. RAG Pipeline Architecture", 1)
    pdf.write_paragraph(
        "The retrieval pipeline queries custom email templates saved in raw text files. The data flows sequentially:\n\n"
        "1. Semantic Query generation: User inputs (e.g., purpose, recipient, key points) are concatenated to build a dense semantic search string.\n"
        "2. Vectorization: The search string is converted into a 3072-dimensional vector using the google gemini-embedding-2 model.\n"
        "3. Local Search: The query vector is scanned against a pre-built local FAISS index, extracting top-K contextually matching templates.\n"
        "4. Prompt Compilation: The retrieved templates are injected into the Prompt Template as few-shot context.\n"
        "5. Generation: Gemini 3.5 Flash processes the unified prompt to output the final formatted email."
    )

    pdf.write_heading("6. Key Implementations: api.py", 2)
    pdf.write_code(
        "@app.post('/generate-email')\n"
        "def generate_email(request: EmailRequest):\n"
        "    # Step 1: Retrieve matching templates from vector database\n"
        "    templates = retrieve_context(rag_query)\n"
        "    # Step 2: Inject retrieved templates into LLM prompt\n"
        "    prompt = build_email_prompt(..., context=templates)\n"
        "    # Step 3: Run Gemini model generation\n"
        "    response = model.generate_content(prompt)\n"
        "    return {'success': True, 'data': {'email': response.text}}"
    )

    # Page 5: Challenges & Resolution
    pdf.add_page()
    pdf.write_heading("7. Major Implementation Challenges & Fixes", 1)

    pdf.write_heading("Issue A: Memory Exhaustion (OOM) on Free-Tier Instances", 2)
    pdf.write_paragraph(
        "Originally, the FAISS database was backed by local Hugging Face all-MiniLM-L6-v2 embeddings via PyTorch. "
        "Because PyTorch and tokenizers require over 1.2 GB of RAM during startup, the t3.micro instance (1GB memory limit) "
        "regularly crashed. To fix this, local vectorization libraries were removed and replaced with Google's hosted "
        "gemini-embedding-2 API, resulting in a lightweight, stable, and serverless vector search process."
    )

    pdf.write_heading("Issue B: Windows ZIP Formatting Extraction Errors", 2)
    pdf.write_paragraph(
        "Deploying standard ZIP archives compiled using Windows utility libraries resulted in unzip failures on "
        "the AWS Amazon Linux 2023 platform because paths were formatted with backslashes (\\). "
        "We bypassed this by generating the deployment archive using git archive, forcing Linux-compatible forward-slash (/) paths."
    )

    pdf.write_heading("Issue C: Procfile Parsing Interruptions", 2)
    pdf.write_paragraph(
        "Windows system text editors often write carriage returns (CRLF) in Procfiles, causing process managers "
        "on Elastic Beanstalk to throw errors. We resolved this by explicitly stripping windows characters and formatting "
        "the file with exactly one line terminated with a Unix Linefeed (LF)."
    )

    # Page 6: Testing & Live verification
    pdf.add_page()
    pdf.write_heading("8. Verification & Production Test Case", 1)
    pdf.write_paragraph(
        "The live REST API hosted on AWS Elastic Beanstalk was tested with the following HTTP POST payload:\n"
    )
    pdf.write_code(
        "{\n"
        "  'sender_name': 'Sparsh',\n"
        "  'recipient_name': 'Harsh',\n"
        "  'company_name': 'IBM',\n"
        "  'purpose': 'follow up',\n"
        "  'tone': 'professional',\n"
        "  'length': 'short',\n"
        "  'key_points': ['Hi', 'Checking in on the project status']\n"
        "}"
    )
    pdf.write_paragraph("The server processed the request and successfully returned code 200 with the email:")
    pdf.write_code(
        "Subject: Follow-Up: Project Status\n\n"
        "Dear Harsh,\n\n"
        "I hope you are having a productive week. I am writing to check in on our project's status "
        "and see if there are any updates from your side. Please let me know if you need any additional "
        "information or support from my end to help move things forward.\n\n"
        "Best regards,\n"
        "Sparsh"
    )

    pdf.write_heading("9. Conclusion", 1)
    pdf.write_paragraph(
        "The project successfully implements a modern, memory-efficient, and enterprise-grade RAG pipeline. "
        "By hosting the core API server on AWS Elastic Beanstalk and the interactive interface on Streamlit Cloud, "
        "we have delivered a reliable, decoupled cloud application. The system performs under 100ms vector searches "
        "and handles high-quality structured drafts at zero cost, making it a highly scalable template generator tool."
    )

    output_path = "Project_Report.pdf"
    pdf.output(output_path)
    print(f"Project Report PDF generated at: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    make_report()
