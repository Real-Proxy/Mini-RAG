import os
import streamlit as st

from src.ingest import ingest_documents,rebuild_index
from src.query import ask_question

st.set_page_config(
    page_title="Mini RAG",
    page_icon="📄",
    layout="wide"
)

st.title("Mini RAG")

UPLOAD_FOLDER = "Uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if not os.listdir(UPLOAD_FOLDER):
    st.info("No documents uploaded yet. Upload documents from the sidebar to get started.")


with st.sidebar:
    st.header("Document Management")

    uploaded_files = st.file_uploader(
        "Upload TXT/PDF Files",
        type=["txt", "pdf"],
        accept_multiple_files=True
    )

    if st.button("Upload & Index"):

        if uploaded_files:

            saved_paths = []

            for uploaded_file in uploaded_files:
                file_path = os.path.join(
                    UPLOAD_FOLDER,
                    uploaded_file.name
                )

                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                saved_paths.append(file_path)

            with st.spinner("Indexing documents..."):
                ingest_documents(saved_paths)

            st.success(f"Indexed {len(saved_paths)} document(s)!")

        else:
            st.warning("Please select at least one file.")
    
    st.subheader("Uploaded Documents")

    uploaded_docs = [
        file for file in os.listdir(UPLOAD_FOLDER)
        if file.lower().endswith((".pdf", ".txt"))
        ]

    if uploaded_docs:
        for i, file in enumerate(uploaded_docs, start=1):
            st.write(f"{i}. {file}")
    else:
        st.caption("No documents uploaded.")

    st.divider()

    if st.button("Rebuild"):
        with st.spinner("Rebuilding Vector Database..."):
            rebuild_index(UPLOAD_FOLDER)
        
        st.success("Vector Database Rebuilded successfully..")


question = st.text_input("Ask a question")

if st.button("Ask"):
    response = ask_question(question)

    if question.strip():
        st.write(response["answer"])
        st.subheader("Sources")
        
        for source in response["sources"]:
            st.write(f"- {source}")
            
    else:
        st.warning("Please enter a question.")