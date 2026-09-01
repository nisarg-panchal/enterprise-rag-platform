from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title="Enterprise RAG Platform",
    version="0.1.0",
    description="Production-oriented Retrieval-Augmented Generation platform.",
)

app.include_router(health_router)


@app.get("/", tags=["system"])
def root() -> dict[str, str]:
    return {
        "name": settings.app_name,
        "version": "0.1.0",
        "status": "running",
    }
