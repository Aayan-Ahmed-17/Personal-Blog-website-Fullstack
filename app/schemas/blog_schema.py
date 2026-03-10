# from pydantic import BaseModel, Field, EmailStr
# from typing import Optional
# from datetime import datetime

# class CreateBlog(BaseModel):
#     """
#     Represents how data is STORED in MongoDB.
#     This is the database document structure.
#     """
#     author_name: str
#     author_email: Optional[EmailStr]
#     title: str
#     description: Optional[str]
#     created_at: datetime = Field(default_factory=datetime.now)
#     updated_at: datetime = Field(default_factory=datetime.now)
    
# from pydantic import BaseModel, EmailStr
# from typing import Optional
# from datetime import datetime


# class BlogCreate(BaseModel):
#     author_name: str
#     author_email: Optional[EmailStr] = None
#     title: str
#     description: str


# class BlogResponse(BaseModel):
#     id: str
#     author_name: str
#     author_email: Optional[str] = None
#     title: str
#     description: str
#     created_at: datetime
#     updated_at: datetime

"""
schemas/blog_schema.py
MongoDB document schema for blog posts.
This represents the actual structure stored in MongoDB.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime


class BlogSchema(BaseModel):
    """
    Schema for blog document stored in MongoDB.
    Defines the complete structure of what's saved in the database.
    
    This includes fields that might not be exposed in API responses.
    """
    
    id: Optional[str] = Field(default=None, alias="_id", description="MongoDB document ID")
    title: str = Field(..., description="Blog post title")
    content: str = Field(..., description="Blog post content")
    author: str = Field(..., description="Author name")
    author_email: Optional[EmailStr] = Field(default=None, description="Author email")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
    

class BlogSchemaUpdate(BaseModel):
    """
    Schema for updating blog documents.
    Only includes updatable fields.
    """
    
    title: Optional[str] = Field(None, description="Blog post title")
    content: Optional[str] = Field(None, description="Blog post content")
    author: Optional[str] = Field(None, description="Author name")
    updated_at: datetime = Field(default_factory=datetime.now, description="Last update timestamp")
    
