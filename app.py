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

    st.divider()

    if st.button("Rebuild"):
        with st.spinner("Rebuilding Vector Database..."):
            rebuild_index(UPLOAD_FOLDER)
        
        st.success("Vector Database Rebuilded successfully..")


question = st.text_input("Ask a question")

if st.button("Ask"):

    if question.strip():

        answer = ask_question(question)

        st.subheader("Answer")

        st.write(answer)

    else:
        st.warning("Please enter a question.")