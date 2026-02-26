from fastapi import APIRouter
from models.blog_model import Blog

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World", "status": "success"}

@router.get("/health")
async def health():
    return {"status": "Api is running", "status_code": 200}

@router.post("/blog")
async def create_blog(blog: Blog):
    return {"message": "Blog created successfully", "blog": blog.model_dump(), "status": "success", "status_code": 201}

# @router.get("/blogs/")
# async def get_blogs():
#     return {"message": "Blogs retrieved successfully", "blogs": [], "status": "success", "status_code": 200}