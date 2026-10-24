import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMMA_MODEL", "gemma-4-26b-a4b-it")

if not api_key:
    print("❌ Error: GEMINI_API_KEY is not set in your .env file.")
    print("👉 Add your Google AI Studio key to .env: GEMINI_API_KEY=your_key")
    exit(1)

print(f"Connecting to Gemma model '{model}' via Google AI Studio...")
client = genai.Client(api_key=api_key)

max_retries = 3
for attempt in range(max_retries):
    try:
        response = client.models.generate_content(
            model=model,
            contents="Explain what an API is in two sentences.",
        )
        print("✅ Connection successful!")
        print(f"Model: {model}")
        print(f"Response:\n{response.text.strip()}")
        break
    except Exception as exc:
        if attempt < max_retries - 1:
            print(f"⚠️ Attempt {attempt + 1} encountered a transient issue ({exc}). Retrying in 2s...")
            time.sleep(2)
        else:
            print("❌ Connection failed after retries!")
            print(f"Details: {exc}")
            print("💡 Please verify your API key, model ID availability in AI Studio, and network connection.")
            exit(1)
