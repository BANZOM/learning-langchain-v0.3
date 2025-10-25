import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

from article import article

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

# messages = [
#     (
#         "system",
#         "you are a helpful assistant that translates English to Hinglish.",
#     ),
#     ("human", "I love programming."),
# ]

# ai_msg = llm.invoke(messages)
# print(ai_msg)

# creative_ai_msg = creative_llm.invoke(messages)
# print(creative_ai_msg)

from langchain.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate

system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an AI assistant that helps generate article titles."
)

user_prompt = HumanMessagePromptTemplate.from_template(
     """You are tasked with creating a name for a article.
The article is here for you to examine 

```article
{article}
```

The name should be based of the context of the article.
Be creative, but make sure the names are clear, catchy,
and relevant to the theme of the article.

Only output the article name, no other explanation or
text can be provided.""",
    input_variables=["article"]
)

from langchain.prompts import ChatPromptTemplate

first_prompt = ChatPromptTemplate.from_messages([
    system_prompt,
    user_prompt
])

print(first_prompt.format(article="Test String"))