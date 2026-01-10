from typing import Optional
from pydantic import BaseModel, Field

class State(BaseModel):
    """State for the workflow graph."""
    query: str = Field(description="The query to write a post about")
    transformed_query: Optional[str] = Field(default=None, description="The transformed query for better engagement")
    generated_post: Optional[str] = Field(default=None, description="The generated post about the query")