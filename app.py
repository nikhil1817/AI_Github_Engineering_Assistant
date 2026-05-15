from fastapi import FastAPI
from pydantic import BaseModel
from repo_tools import clone_repo, read_repo_files
from rag import build_repo_index
from agent import answer_repo_question

app = FastAPI()


class CloneRequest(BaseModel):
    repo_url: str
    repo_name: str


class AskRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "AI GitHub Engineering Assistant is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/clone")
def clone_and_index_repo(request: CloneRequest):
    repo_path = clone_repo(request.repo_url, request.repo_name)
    files = read_repo_files(repo_path)
    chunks_count = build_repo_index(files)

    return {
        "message": "Repository cloned and indexed successfully",
        "repo_path": repo_path,
        "files_read": len(files),
        "chunks_created": chunks_count
    }


@app.post("/ask")
def ask_question(request: AskRequest):
    return answer_repo_question(request.question)
