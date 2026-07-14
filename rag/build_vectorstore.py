import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
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

    
    # Use local HuggingFaceEmbeddings since sentence-transformers is installed.
    # This runs completely offline and avoids Hugging Face Hub server outages.
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    
    vectorstore = FAISS.from_documents(split_docs, embeddings)

    vectorstore.save_local("faiss_index")

    print("Vectorstore built successfully using HuggingFace embeddings!")

if __name__ == "__main__":
    build_vectorstore()