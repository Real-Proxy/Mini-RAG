from langchain_postgres import PGVector
from sqlalchemy import create_engine,text

from src.config import DATABASE_URL
from src.embeddings import embeddings

COLLECTION_NAME = "documents"

engine = create_engine(DATABASE_URL)

vector_store = PGVector(
    embeddings=embeddings,
    collection_name=COLLECTION_NAME,
    connection=DATABASE_URL,
    use_jsonb=True,
)

def clear_embeddings():
    query=text(f"""DELETE FROM langchain_pg_embedding
        WHERE collection_id = (
            SELECT uuid
            FROM langchain_pg_collection
            WHERE name = :collection_name
        );
        """)
    with engine.begin() as conn:
        conn.execute(
            query,
            {"collection_name": COLLECTION_NAME}
        )

    print("Embeddings cleared.")
