from fastapi import APIRouter
# from app.schemas.blog_schema import BlogSchema, BlogSchemaUpdate
from app.models.blog_model import BlogModel
from app.services.crud.blog_crud import create_blog # type: ignore

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


@router.post("/", response_model=None)
async def post_blog(blog: BlogModel):
    """
    is the code updated successfully
    """
    return create_blog(blog) # type: ignore
    


@router.get("/")
async def get_blogs():
    """Retrieves all blog blogs from the database and returns them as a list."""
    return {"message": "Retrieving all blog blogs"}


@router.get("/{id}")
async def read_blog(id: str):
    """Retrieves a specific blog post by its ID."""
    return {"message": f"Retrieving blog with ID: {id}"}


# @router.put("/{id}")
# async def update_blog(id: str, blog: BlogCreate):  # type: ignore
#     """Updates a specific blog post by its ID."""
#     return {"message": f"Updating blog with ID: {id}", "updated_blog": blog}


@router.delete("/{id}")
async def delete_blog(id: str):
    """Deletes a specific blog post by its ID."""
    return {"message": f"Deleting blog with ID: {id}"}
