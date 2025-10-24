import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.4,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=GEMINI_API_KEY
    # other params...
)

creative_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.9,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=GEMINI_API_KEY
    # other params...
)

messages = [
    (
        "system",
        "you are a helpful assistant that translates English to Hinglish.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg)

creative_ai_msg = creative_llm.invoke(messages)
print(creative_ai_msg)
