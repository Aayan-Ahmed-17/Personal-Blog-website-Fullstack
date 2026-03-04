from bs4 import BeautifulSoup, Tag
from typing import List
from .scrape import get_data, url, headers
from .models import BlogPost
from . import selectors as sel
from .extractors import (
    extract_blog_link,
    extract_img_link,
    extract_title,
    extract_latest_date,
    extract_description,
)

response = get_data(url, headers=headers)

def parse_blog_container(container: Tag) -> BlogPost:
    return BlogPost(
        blog_link   = extract_blog_link(container), # type: ignore
        img_link    = extract_img_link(container), # type: ignore
        title       = extract_title(container), # type: ignore
        latest_date = extract_latest_date(container), # type: ignore
        description = extract_description(container), # type: ignore
    )


def parse_all_blogs(html) -> List[BlogPost]:
    soup = BeautifulSoup(html.content, "html.parser")
    grid = soup.select_one(sel.BLOG_GRID_CONTAINER)

    if not grid:
        return []

    containers = grid.select(sel.BLOG_CONTAINER)   # your 45 containers
    return [parse_blog_container(c) for c in containers]
