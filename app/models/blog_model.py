from datetime import datetime
from typing import Optional


class BlogModel:
    def __init__(
        self,
        author_name: str,
        title: str,
        description: str,
        author_email: Optional[str] = None,
    ):
        self.author_name = author_name
        self.author_email = author_email
        self.title = title
        self.description = description
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "author_name": self.author_name,
            "author_email": self.author_email,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }