from src.routes.generate_post import generate_post
from src.routes.generate_post import PostRequest, PostResponse
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Agentic Post Studio API", version="1.0.0")


@app.get("/")
def read_root():
    return {
        "message": "Welcome to Agentic Post Studio API",
        "endpoints": ["/docs", "/generate-post"],
    }


@app.get("/health")
def health_check():
    """Check if the API is running."""
    return {"status": "healthy", "service": "agentic-post-studio"}


@app.post("/generate-post", response_model=PostResponse)
async def generate_post_route(request: PostRequest):
    """Generate a post based on the provided query."""
    return await generate_post(request)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
