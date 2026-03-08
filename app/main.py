from app.api.v1.endpoints.blogs import router as blogs_router
from app.api.v1.endpoints.scraper import router as scraper_router
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Template",
    description="A simple FastAPI template for building APIs",
    version="1.0.0",
)

app.include_router(blogs_router, prefix="/api/v1")
app.include_router(scraper_router, prefix="/api/v1")
