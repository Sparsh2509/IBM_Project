import os
import requests
from langchain_core.embeddings import Embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
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


def build_vectorstore():
    loader = DirectoryLoader(
        "Email_Templates_idea",
        glob="**/*.txt",
        loader_cls=TextLoader
    )

    docs = loader.load()
    print(f"Loaded {len(docs)} documents")
    print(docs[0])
    print(docs[0].page_content)
    print(docs[0].metadata)

    for doc in docs:
        filename = os.path.basename(doc.metadata["source"])
        doc.metadata["filename"] = filename

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    split_docs = splitter.split_documents(docs)

    # Use HF Inference API for embeddings — no PyTorch needed on the server.
    embeddings = HFInferenceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(split_docs, embeddings)
    vectorstore.save_local("faiss_index")

    print("Vectorstore built successfully using HF Inference API embeddings!")


if __name__ == "__main__":
    build_vectorstore()