from fastapi import FastAPI
from .routes import router

app = FastAPI(title="FastAPI Template", description="A simple FastAPI template for building APIs", version="1.0.0")
app.include_router(router)