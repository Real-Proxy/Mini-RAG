from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.vector_store import vector_store
from src.utils import load_document
import os


def ingest_documents(file_paths):
    """
    Ingest one or more TXT/PDF documents into PGVector.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
    )

    all_chunks = []

    for file_path in file_paths:

        documents = load_document(file_path)
        chunks = splitter.split_documents(documents)

        filename = os.path.basename(file_path)

        # Add metadata to every chunk
        for chunk in chunks:
            chunk.metadata["source"] = filename

        print(f"\nProcessed: {filename}")
        print(f"Documents : {len(documents)}")
        print(f"Chunks    : {len(chunks)}")

        all_chunks.extend(chunks)

    print("=" * 60)
    print(f"Total Chunks: {len(all_chunks)}")

    vector_store.add_documents(all_chunks)

    print(f"Ingested {len(all_chunks)} chunks into PGVector.")


if __name__ == "__main__":
    ingest_documents(["Data/employee_handbook.txt"])