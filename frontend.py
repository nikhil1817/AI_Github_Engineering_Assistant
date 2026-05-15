import streamlit as st
import requests

st.title("AI GitHub Engineering Assistant")

repo_url = st.text_input("GitHub Repo URL")
repo_name = st.text_input("Local Repo Name", "my_repo")

if st.button("Clone and Index Repo"):
    response = requests.post(
        "http://127.0.0.1:8000/clone",
        json={
            "repo_url": repo_url,
            "repo_name": repo_name
        }
    )

    st.write("Status:", response.status_code)

    try:
        st.json(response.json())
    except Exception:
        st.text(response.text)

question = st.text_input("Ask a question about the repo")

if st.button("Ask"):
    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"question": question}
    )

    try:
        result = response.json()

        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("Sources")
        for source in result["sources"]:
            st.write(source["path"])
            st.code(source["content"][:1000])

    except Exception:
        st.error("Backend did not return JSON")
        st.text(response.text)
