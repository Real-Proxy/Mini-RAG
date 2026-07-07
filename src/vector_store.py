from langchain_postgres import PGVector

from src.config import DATABASE_URL
from src.embeddings import embeddings

COLLECTION_NAME = "employee_handbook"

vector_store = PGVector(
    embeddings=embeddings,
    collection_name=COLLECTION_NAME,
    connection=DATABASE_URL,
    use_jsonb=True,
)