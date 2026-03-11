from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


class CreateBlog(BaseModel):
    author_name: str = Field(
        ..., min_length=3, max_length=16, description="Enter AUthor name"
    )
    author_email: EmailStr | None = Field(
        None, description="An optional email address for contact."
    )
    title: str = Field(..., min_length=3, description="Enter Blog Title Here...")
    description: str = Field(..., description="Enter Blog Description Here...")
    created_at : datetime = Field(default_factory=datetime.now)
    updated_at : datetime = Field(default_factory=datetime.now)
    
class UpdateBlog(BaseModel):
    title: str = Field(..., min_length=3, description="Enter Blog Title Here...")
    description: str = Field(..., description="Enter Blog Description Here...")
    updated_at : datetime = Field(default_factory=datetime.now)
