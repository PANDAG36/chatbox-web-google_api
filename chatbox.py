import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
gemini_key = os.getenv("GOOGLE_API_KEY")

# print(gemini_key)

client = genai.Client(api_key = gemini_key)

def chatresponse(chat_request, model="gemini-2.5-flash"):
    try:
        response = client.models.generate_content(
            model=model,
            contents=chat_request
        )
        return response.text, model
    except Exception as e:
        return f"Error: {str(e)}", model
