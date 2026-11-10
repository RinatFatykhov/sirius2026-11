from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
API_KEY = os.getenv('API_KEY')
MODEL = os.getenv('MODEL')

client = OpenAI(
    base_url=API_URL,
    api_key=API_KEY
)


def call_llm(messages: list) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        extra_body={'chat_template_kwargs': {'enable_thinking': False}}
    )
    return response.choices[0].message.content
