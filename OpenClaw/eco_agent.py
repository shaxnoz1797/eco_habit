from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Yangi kutubxona bilan client yaratish
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_eco_agent():
    try:
        # Ishlayotgan modelni yozamiz
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents="Ekologik odatlar haqida tahlil ber..."
        )
        print(response.text)
    except Exception as e:
        print(f"Xato: {e}")

if __name__ == "__main__":
    run_eco_agent()