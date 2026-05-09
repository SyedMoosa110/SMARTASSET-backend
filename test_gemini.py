import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print(f"Testing with key: {api_key[:10]}...")
genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel('gemini-flash-latest')
    response = model.generate_content("Hello, say 'Test Success'")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
