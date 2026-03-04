from app.api.v1.routers.articles.online import router as online_router
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Template",
    description="A simple FastAPI template for building APIs",
    version="1.0.0",
)

app.include_router(online_router, prefix="/api/v1/blogs", tags=["Online Blogs"])
