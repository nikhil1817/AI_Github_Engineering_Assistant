import os
from git import Repo

ALLOWED_EXTENSIONS = {
    ".py", ".js", ".ts", ".java", ".md", ".txt", ".json", ".yml", ".yaml"
}


def clone_repo(repo_url: str, repo_name: str):
    repo_path = os.path.join("repos", repo_name)

    if os.path.exists(repo_path):
        return repo_path

    Repo.clone_from(repo_url, repo_path)
    return repo_path


def read_repo_files(repo_path: str):
    files = []

    for root, _, filenames in os.walk(repo_path):
        if ".git" in root:
            continue

        for filename in filenames:
            ext = os.path.splitext(filename)[1]

            if ext not in ALLOWED_EXTENSIONS:
                continue

            path = os.path.join(root, filename)

            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                files.append({
                    "path": path,
                    "content": content
                })

            except Exception:
                pass

    return files
