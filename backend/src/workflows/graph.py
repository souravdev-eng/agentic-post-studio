from langgraph.graph import StateGraph, START, END
from src.workflows.state import State
from src.workflows.nodes.transformer_node import transformer_node
from src.workflows.nodes.generate_node import generate_post_node


# Create the graph
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
# compiled_graph.get_graph().draw_mermaid_png(output_file="workflow.png")

# if __name__ == "__main__":
#     # Test the workflow
#     test_query = "What is the capital of France?"
#     print(f"Query: {test_query}")
#     print("-" * 50)
    
#     try:
#         result = compiled_graph.invoke({"query": test_query})
#         print("Generated Post:")
#         print(result.get("transformed_query", "No transformed query generated"))
#     except Exception as e:
#         print(f"Error: {e}")
#         print("\nMake sure to set the OPENAI_API_KEY environment variable before running this script.")