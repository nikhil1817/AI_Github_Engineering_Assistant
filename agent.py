import os
from dotenv import load_dotenv
from openai import OpenAI
from rag import retrieve_code

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def answer_repo_question(question: str):
    chunks = retrieve_code(question)

    if not chunks:
        return {
            "answer": "No repository indexed yet.",
            "sources": []
        }

    context = ""

    for i, chunk in enumerate(chunks, 1):
        context += f"\n--- Source {i}: {chunk['path']} ---\n"
        context += chunk["content"] + "\n"

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": (
                    "You are an AI GitHub engineering assistant. "
                    "Explain code clearly. Use only the provided repository context. "
                    "If the answer is not in the context, say you could not find it in the repo."
                )
            },
            {
                "role": "user",
                "content": f"Repository context:\n{context}\n\nQuestion:\n{question}"
            }
        ]
    )

    return {
        "answer": response.output_text,
        "sources": chunks
    }
