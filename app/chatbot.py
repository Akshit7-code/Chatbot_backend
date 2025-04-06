
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

# Load the key from the environment
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(COHERE_API_KEY)

def get_response(message):
    response = co.chat(
        message=message,
        model="command-r",  # You can also try "command-r-plus"
        temperature=0.5
    )
    return response.text

