import os
from dotenv import load_dotenv
from openai import OpenAI
import chromadb

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chroma_client = chromadb.Client()

collection = None


def chunk_text(text: str, chunk_size: int = 1200, overlap: int = 200):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def get_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


def build_repo_index(files):
    global collection

    try:
        chroma_client.delete_collection(name="repo_code")
    except Exception:
        pass

    collection = chroma_client.get_or_create_collection(name="repo_code")

    ids = []
    docs = []
    metadatas = []
    embeddings = []

    count = 0

    for file in files:
        path = file["path"]
        content = file["content"]

        for chunk in chunk_text(content):
            ids.append(str(count))
            docs.append(chunk)
            metadatas.append({"path": path})
            embeddings.append(get_embedding(chunk))
            count += 1

    if ids:
        collection.add(
            ids=ids,
            documents=docs,
            embeddings=embeddings,
            metadatas=metadatas
        )

    return count


def retrieve_code(query: str, top_k: int = 5):
    if collection is None:
        return []

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    chunks = []

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    for doc, metadata in zip(documents, metadatas):
        chunks.append({
            "path": metadata["path"],
            "content": doc
        })

    return chunks
