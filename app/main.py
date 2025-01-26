from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.config import settings  # optional config usage


def create_app() -> FastAPI:
    app = FastAPI(
        title="persian crypto exchanges jobinform API",
        version="1.0.0",
    )
    app.include_router(api_router)
    return app


app = create_app()
