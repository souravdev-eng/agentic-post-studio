from src.workflows.state import State
from src.chains.generate import generate_chain


def generate_post_node(state: State) -> dict:
    """Generate a post about the transformed query."""
    generated_post = generate_chain.invoke(
        {"transformed_query": state.transformed_query}
    )
    return {"generated_post": generated_post}
