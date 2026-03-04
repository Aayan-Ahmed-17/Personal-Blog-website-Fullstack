from dataclasses import dataclass

@dataclass
class BlogPost:
    blog_link: str
    img_link: str
    title: str
    latest_date: str
    description: str