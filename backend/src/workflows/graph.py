from langgraph.graph import StateGraph, START, END
from src.workflows.state import State
from src.workflows.nodes.transformer_node import transformer_node
from src.workflows.nodes.generate_node import generate_post_node

graph = StateGraph(State)

# Add nodes
graph.add_node("transformer", transformer_node)
graph.add_node("generate_post", generate_post_node)

# Add edges
graph.add_edge(START, "transformer")
graph.add_edge("transformer", "generate_post")
graph.add_edge("generate_post", END)

# Compile the graph
compiled_graph = graph.compile()
