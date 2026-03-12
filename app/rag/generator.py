from langchain_openai import ChatOpenAI
from app.core.config import settings


def get_llm(streaming: bool = False):

    return ChatOpenAI(
        model="openai/gpt-5-nano",
        api_key=settings.OPENAI_API_KEY,
        base_url="https://openrouter.ai/api/v1",
        temperature=0,
        streaming=streaming
    )