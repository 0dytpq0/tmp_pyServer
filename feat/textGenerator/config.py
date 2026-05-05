import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))
MODEL = "gemini-3-flash-preview"