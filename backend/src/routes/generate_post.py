from fastapi import HTTPException
from pydantic import BaseModel
from workflows.graph import compiled_graph


class PostRequest(BaseModel):
    query: str


class PostResponse(BaseModel):
    query: str
    transformed_query: str
    generated_post: str


async def generate_post(request: PostRequest):
    """Generate a post based on the provided query."""
    try:
        # Validate input
        if not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")

        # Invoke the workflow with the query
        result = compiled_graph.invoke({"query": request.query})

        # Validate output
        if not result.get("generated_post"):
            raise HTTPException(status_code=500, detail="Failed to generate post")

        return PostResponse(
            query=request.query,
            transformed_query=result.get("transformed_query", ""),
            generated_post=result.get("generated_post", ""),
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
