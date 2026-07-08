from src.vector_store import vector_store
from src.llm import llm

def ask_question(query):

    results = vector_store.similarity_search(query=query, k=5)

    print("\nRetrieved Chunks")
    print("=" * 60)

    for i, doc in enumerate(results):
        print(f"\nChunk {i+1}")
        print("-" * 40)
        print(doc.page_content)

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

    sources = []

    for doc in results:
        source = doc.metadata.get("source", "Unknown")

    if source not in sources:
        sources.append(source)
        return {"answer": response.content[0]["text"],"sources": sources}

