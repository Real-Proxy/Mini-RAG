from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.vector_store import vector_store,clear_embeddings
from src.utils import load_document
import os


def ingest_documents(file_paths):
    """
    Ingest one or more TXT/PDF documents into PGVector.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
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


def rebuild_index(upload_folder):
    clear_embeddings()

    file_paths=[]

    for file in os.listdir(upload_folder):
        if file.lower().endswith((".txt",".pdf")):
            file_paths.append(os.path.join(upload_folder,file))
        

    if not file_paths:
        print("No documents founds")
        return    
        
    ingest_documents(file_paths)   
    


if __name__ == "__main__":
    ingest_documents(["Data/employee_handbook.txt"])