from fastapi import FastAPI
from .routers import blogs

app = FastAPI(title="FastAPI Template", description="A simple FastAPI template for building APIs", version="1.0.0")
app.include_router(blogs.router, prefix="/api/v1/blogs", tags=["Blogs"])