from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_template(
"""
You are an knowledge assistant.

Use the conversation history and the provided context
to answer the user's question.

If the answer is not in the context, say:
"I could not find that information in the company documents."

Conversation History:
{history}

Context:
{context}

Question:
{question}

Answer:
"""
)