from fastapi import FastAPI
from pydantic import BaseModel
from rag.retriever import retrieve_context       
from prompts.email_prompt import build_email_prompt       
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    generation_config={"temperature": 0.7}  
)

class EmailRequest(BaseModel):
    sender_name: str
    recipient_name: str
    company_name: str
    purpose: str
    tone: str
    length: str
    key_points: list[str]

@app.get("/")
def root():
    return {"message": "AI Email Generator API is running"}

@app.post("/generate-email")
def generate_email(request: EmailRequest):
    try:
        # Build a rich semantic query from all available request fields so the
        # vector retrieval surfaces examples that are contextually relevant to
        # the specific purpose, tone, recipient, and key points — not just a
        # generic purpose label.
        key_points_preview = " ".join(request.key_points)[:200] if request.key_points else ""
        query_parts = [
            f"{request.purpose} email",
            f"tone: {request.tone}",
            f"length: {request.length}",
            f"recipient: {request.recipient_name}",
            f"company: {request.company_name}",
        ]
        if key_points_preview:
            query_parts.append(f"key points: {key_points_preview}")
        rag_query = " | ".join(query_parts)

        templates = retrieve_context(rag_query)
        key_points_str = "\n".join(f"- {point}" for point in request.key_points)

        prompt = build_email_prompt(
            sender_name=request.sender_name,
            recipient_name=request.recipient_name,
            company_name=request.company_name,
            purpose=request.purpose,
            tone=request.tone,
            length=request.length,
            key_points=key_points_str,
            context=templates
        )

        response = model.generate_content(prompt)

        return {
            "success": True,
            "data": {
                "email": response.text
            }
        }

    except Exception as e:
        return {
            "success": False,
            "data": None,
            "error": str(e)
        }