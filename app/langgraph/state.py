from typing import TypedDict


class GraphState(TypedDict):

    question: str
    history: str
    prompt:str    
    query_type: str
    docs: list
    answer: str