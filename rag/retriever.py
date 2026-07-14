from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

from dotenv import load_dotenv
load_dotenv()

# Use local HuggingFaceEmbeddings since sentence-transformers is installed.
# This runs completely offline and avoids Hugging Face Hub server outages.
embeddings = HuggingFaceEmbeddings(
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