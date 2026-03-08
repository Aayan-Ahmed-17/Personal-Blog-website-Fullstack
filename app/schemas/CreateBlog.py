from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class CreateBlog(BaseModel):
    """
    Represents how data is STORED in MongoDB.
    This is the database document structure.
    """
    author_name: str
    author_email: EmailStr
    title: str
    description: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)