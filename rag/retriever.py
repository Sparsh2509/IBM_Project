import os
import requests
from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()


class HFInferenceEmbeddings(Embeddings):
    """Lightweight embeddings via HuggingFace Inference API — no PyTorch needed."""

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.hf_token = os.getenv("HF_TOKEN")
        self.api_url = (
            f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_name}"
        )
        self.headers = {}
        if self.hf_token:
            self.headers["Authorization"] = f"Bearer {self.hf_token}"

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        response = requests.post(
            self.api_url,
            headers=self.headers,
            json={"inputs": texts, "options": {"wait_for_model": True}},
        )
        if response.status_code != 200:
            raise Exception(f"HF API Error: {response.status_code} — {response.text}")
        return response.json()

    def embed_query(self, text: str) -> list[float]:
        return self.embed_documents([text])[0]


embeddings = HFInferenceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})


def retrieve_context(query: str) -> str:
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs])