from src.workflows.state import State
from src.chains.transformer import transformer_chain


def transformer_node(state: State) -> dict:
    """Process the query and transform it for better engagement."""
    transformed_query = transformer_chain.invoke({"query": state.query})
    return {"transformed_query": transformed_query}
