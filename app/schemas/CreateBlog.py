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
    
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class BlogCreate(BaseModel):
    author_name: str
    author_email: Optional[EmailStr] = None
    title: str
    description: str


class BlogResponse(BaseModel):
    id: str
    author_name: str
    author_email: Optional[str] = None
    title: str
    description: str
    created_at: datetime
    updated_at: datetime