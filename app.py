import streamlit as st

from src.query import ask_question

st.set_page_config(
    page_title="Mini RAG",
    page_icon="📄",
    layout="wide"
)

st.title("Mini RAG")

question = st.text_input("Ask a question")

if st.button("Ask"):

    if question.strip():

        answer = ask_question(question)

        st.subheader("Answer")

        st.write(answer)

    else:
        st.warning("Please enter a question.")