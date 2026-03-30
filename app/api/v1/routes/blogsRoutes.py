from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.models.blog_model import CreateBlog, UpdateBlog
from app.services.crud.blog_crud import create_blog, update_blog, get_all_blogs, get_blog_by_id, delete_blog  # type: ignore

router = APIRouter(
    prefix="/blogs",  # All paths in this router will start with "/blogs"
    tags=["Blogs"],  # Adds a tag for documentation in /docs
)

"""
Handles CRUD operations of Self Blogs. 
POST /api/blogs/: Create a new blog post.
GET /api/blogs/: Retrieve all blog blogs.
GET /api/blogs/{id}: Read a specific blog post.
PUT /api/blogs/{id}: Update a blog post.
DELETE /api/blogs/{id}: Delete a blog post.
"""


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_blog(blog: CreateBlog):  # type: ignore
    return create_blog(blog)  # type: ignore


@router.get("/")
async def get_blogs():
    """Retrieves all blog blogs from the database and returns them as a list."""
    return get_all_blogs()


@router.get("/{id}")
async def read_blog(id: str):
    """Retrieves a specific blog post by its ID."""
    return get_blog_by_id(id)


@router.put("/{id}")
async def update_blog_endpoint(id: str, blog_data: UpdateBlog):
    return update_blog(id=id, blog_data=blog_data)  # type: ignore


@router.delete("/{id}")
async def delete_blog_endpoint(id: str):
    """Deletes a specific blog post by its ID."""
    return delete_blog(id)
