import os
import time

from langchain_google_genai._common import GoogleGenerativeAIError
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.vector_store import vector_store, clear_embeddings
from src.utils import load_document

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

    BATCH_SIZE = 20

    for i in range(0, len(all_chunks), BATCH_SIZE):
        batch = all_chunks[i:i + BATCH_SIZE]
        
        while True:
            try:
                vector_store.add_documents(batch)
                print(
                    f"Indexed batch "
                    f"{i//BATCH_SIZE + 1} "
                    f"({len(batch)} chunks)"
                    )

                break

            except GoogleGenerativeAIError as e:
                if "RESOURCE_EXHAUSTED" in str(e):
                    print("\nRate limit reached.")
                    print("Waiting 5 seconds before retrying...\n")

                    time.sleep(5)

                else:
                    raise e

    print(f"\nSuccessfully ingested {len(all_chunks)} chunks into PGVector.")

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