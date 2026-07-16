import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# FastAPI backend URL — reads from env var or streamlit secrets
API_URL = os.getenv("API_URL") or st.secrets.get("API_URL") or "http://localhost:8000"

st.set_page_config(page_title="AI Email Copilot", page_icon="📧")

st.title("📧 AI Email Copilot (RAG Powered)")
st.write("Generate professional emails using Retrieval-Augmented Generation.")

# INPUT FORM
with st.form("email_form"):
    sender = st.text_input("Sender Name")
    recipient = st.text_input("Recipient Name")
    company = st.text_input("Company Name")

    purpose = st.selectbox(
        "Purpose",
        ["cold email", "internship request", "follow up", "apology", "sales outreach"]
    )

    tone = st.selectbox(
        "Tone",
        ["professional", "friendly", "persuasive", "formal", "confident"]
    )

    length = st.selectbox(
        "Length",
        ["short", "medium", "long"]
    )

    key_points = st.text_area(
        "Key Points (Write bullet points, one per line)"
    )

    submit_button = st.form_submit_button("Generate Email")


# GENERATION LOGIC
if submit_button:

    if not sender or not recipient or not company:
        st.warning("Please fill all required fields.")
        st.stop()

    if not key_points.strip():
        key_points = "No specific key points provided. Write a general email."

    with st.spinner("Retrieving context and generating email..."):
        try:
            response = requests.post(
                f"{API_URL}/generate-email",
                json={
                    "sender_name": sender,
                    "recipient_name": recipient,
                    "company_name": company,
                    "purpose": purpose,
                    "tone": tone,
                    "length": length,
                    "key_points": [kp.strip() for kp in key_points.split("\n") if kp.strip()]
                },
                timeout=60
            )

            result = response.json()

            if result.get("success"):
                st.success("Email Generated Successfully!")
                st.markdown("### Generated Email")
                st.text_area("Output", result["data"]["email"], height=400)
            else:
                st.error(f"API Error: {result.get('error', 'Unknown error')}")

        except requests.exceptions.ConnectionError:
            st.error(
                f"❌ Cannot connect to the backend API at `{API_URL}`.\n\n"
                "Please ensure the FastAPI server is running on AWS Elastic Beanstalk."
            )
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")