from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    google_api_key=GEMINI_API_KEY,
    temperature=0
)