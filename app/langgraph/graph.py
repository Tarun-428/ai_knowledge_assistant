from langgraph.graph import StateGraph

from app.langgraph.state import GraphState
from app.langgraph.nodes.router_node import router_node
from app.langgraph.nodes.rag_node import rag_node
from app.langgraph.nodes.summary_node import summary_node


builder = StateGraph(GraphState)

builder.add_node("router", router_node)
builder.add_node("rag", rag_node)
builder.add_node("summary", summary_node)

builder.set_entry_point("router")


builder.add_conditional_edges(
    "router",
    lambda x: x["query_type"],
    {
        "rag": "rag",
        "summary": "summary"
    }
)

builder.set_finish_point("rag")
builder.set_finish_point("summary")

graph = builder.compile()