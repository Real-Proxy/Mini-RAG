from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Read environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Validate configuration
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL not found in .env")

if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY not found in .env")