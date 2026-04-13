# from app.api.v1.endpoints.blogs import router as blogs_router
from fastapi import FastAPI
from app.api.v1.routes import blogsRoutes, scraper
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastAPI Template",
    description="A simple FastAPI template for building APIs",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permits all origins
    allow_credentials=True,
    allow_methods=["*"],  # Permits all methods
    allow_headers=["*"],  # Permits all headers
)

# Add root endpoint
@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "message": "Personal Blog API is running",
        "version": "1.0.0"
    }

# Add health check endpoint
@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}

app.include_router(blogsRoutes.router, prefix="/api/v1")
app.include_router(scraper.router, prefix="/api/v1")
