def ingest_documents():
    from langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from vector_store import vector_store

    loader = TextLoader("Data/employee_handbook.txt")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
    )

    chunks = splitter.split_documents(documents)

    print(f"Original Documents : {len(documents)}")
    print(f"Chunks Created     : {len(chunks)}")
    print("=" * 60)

    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i+1}")
        print("-" * 40)
        print(chunk.page_content)

    vector_store.add_documents(chunks)
    print(f"Ingested {len(chunks)} chunks into PGVector.")

if __name__ == "__main__":
    ingest_documents()