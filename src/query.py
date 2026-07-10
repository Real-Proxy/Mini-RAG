from src.vector_store import vector_store
from src.llm import llm

def ask_question(query):

    results = vector_store.similarity_search(query=query,k=5)

    print("\nRetrieved Chunks")
    print("=" * 60)

    for i, doc in enumerate(results):
        print(f"\nChunk {i+1}")
        print("-" * 40)
        print(doc.page_content)

    contexts = [doc.page_content for doc in results]

    context = "\n\n".join(contexts)

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
    
    print(type(response.content))
    print(response.content)

    sources = []

    for doc in results:
        source = doc.metadata.get("source", "Unknown")

        if source not in sources:
            sources.append(source)

    # Extract plain text regardless of Gemini response format
    if isinstance(response.content, str):
        answer = response.content

    elif isinstance(response.content, list):
        answer_parts = []

        for item in response.content:
            if isinstance(item, dict):
                answer_parts.append(item.get("text", ""))
            else:
                answer_parts.append(str(item))

        answer = "\n".join(answer_parts)

    else:
        answer = str(response.content)

    return {
        "answer": answer,
        "sources": sources,
        "contexts": contexts,
        }