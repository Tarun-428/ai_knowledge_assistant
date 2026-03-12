from app.services.query_router import detect_query_type
from app.rag.generator import get_llm


def router_node(state):

    question = state["question"]
    llm = get_llm()
    # query_type = detect_query_type(question)
    prompt = f"""
        based on user query you have to decide 
        Return ONLY one word:
        -summary
        -rag
        user want to summarize the document of anything else
        focus on his question 
        example: if he tells to summarize the last message then it should return word rag,
        only return word summary if user says goal of docs, idea of document,summary of document

        User query:
        {question}
    """
    query_type=llm.invoke(prompt)
    print(query_type.content)
    return {
        "query_type": query_type.content,
        "history": state.get("history","")
    }