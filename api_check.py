import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

gemini_api = os.getenv("GEMINI_API_KEY")
if not gemini_api:
    raise ValueError("API Key not found in environment Variable")
genai.configure(api_key=gemini_api) # type: ignore
model = genai.GenerativeModel('gemini-2.5-flash')

response = model.generate_content("What is the capital of France?")

print(response.text.strip())