from src.workflows.graph import compiled_graph


if __name__ == "__main__":
    # compiled_graph.get_graph().draw_mermaid_png(output_file="workflow.png")
    query = "Write a post about how I turn from a supermarket sales boy to an Software Engineer."
    result = compiled_graph.invoke({"query": query})
    print(f"Query: {query}")
    print("-" * 50)
    print("Generated Post:")
    print(result.get("generated_post", "No generated post"))
