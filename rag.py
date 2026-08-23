import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.tools import tool
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Load .env
load_dotenv()


POLICY_FILE = "policy.txt"
VECTOR_FOLDER = "faiss_index"


def create_rag():

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found. Check your .env file."
        )

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key
    )

    if Path(VECTOR_FOLDER).exists():

        vectorstore = FAISS.load_local(
            VECTOR_FOLDER,
            embeddings,
            allow_dangerous_deserialization=True
        )

        return vectorstore

    text = Path(POLICY_FILE).read_text(
        encoding="utf-8"
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = splitter.create_documents([text])

    vectorstore = FAISS.from_documents(
        documents,
        embeddings
    )

    vectorstore.save_local(VECTOR_FOLDER)

    return vectorstore


vectorstore = create_rag()


@tool
def search_company_policy(question: str) -> str:
    """Search company policy for returns, refunds, cancellation, shipping, delivery, and privacy questions."""

    documents = vectorstore.similarity_search(
        question,
        k=3
    )

    if not documents:
        return "No relevant company policy was found."

    return "\n\n".join(
        document.page_content
        for document in documents
    )