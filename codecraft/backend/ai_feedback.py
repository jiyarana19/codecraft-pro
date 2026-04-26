import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found. Add it in .env file")

client = Groq(api_key=api_key)

def get_feedback(code):
    prompt = f"""
    You are a web development mentor.

    Analyze this code and give:
    1. Mistakes
    2. Improvements
    3. Suggestions

    Code:
    {code}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content