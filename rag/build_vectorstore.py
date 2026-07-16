import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


def build_vectorstore():
    loader = DirectoryLoader(
        "Email_Templates_idea",
        glob="**/*.txt",
        loader_cls=TextLoader
    )

    docs = loader.load()
    print(f"Loaded {len(docs)} documents")

    for doc in docs:
        filename = os.path.basename(doc.metadata["source"])
        doc.metadata["filename"] = filename

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    split_docs = splitter.split_documents(docs)

    # Use GoogleGenerativeAIEmbeddings (Gemini text-embedding-004) to match the retriever
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    vectorstore = FAISS.from_documents(split_docs, embeddings)
    vectorstore.save_local("faiss_index")

    print("Vectorstore built successfully using Google Generative AI embeddings!")


if __name__ == "__main__":
    build_vectorstore()