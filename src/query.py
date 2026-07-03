from vector_store import vector_store
from llm import llm

def ask_question(query):

    results = vector_store.similarity_search(query=query, k=2)

    context = "\n\n".join([doc.page_content for doc in results])

    prompt = f"""
    You are a helpful HR assistant.

    Answer ONLY using the provided context.

    If the answer is not present in the context, reply:

    "I couldn't find that information in the uploaded documents."

    Do not make up information.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content[0]["text"]

