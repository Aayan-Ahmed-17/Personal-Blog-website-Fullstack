from fastapi import APIRouter
from app.schemas.CreateBlog import CreateBlog

router = APIRouter()

@router.post("/blogs")
async def create_blog(blog: CreateBlog): # type: ignore
    return {"message": "Blog created successfully", "blog": blog}