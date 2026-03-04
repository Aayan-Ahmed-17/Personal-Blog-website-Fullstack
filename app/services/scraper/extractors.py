from bs4 import Tag
from typing import Optional
from . import selectors as sel


def extract_blog_link(container: Tag) -> Optional[str]:
    tag = container.select_one(sel.BLOG_LINK)
    return tag.get("href") if tag else None


def extract_img_link(container: Tag) -> Optional[str]:
    tag = container.select_one(sel.IMG_TAG)
    return tag.get("src") if tag else None


def extract_title(container: Tag) -> Optional[str]:
    tag = container.select_one(sel.TITLE_TAG)
    return tag.text.strip() if tag else None


def extract_latest_date(container: Tag) -> Optional[str]:
    tags = container.select(sel.DATE_TAG)
    return tags[1].text.strip() if len(tags) > 1 else None


def extract_description(container: Tag) -> Optional[str]:
    tag = container.select_one(sel.DESCRIPTION_TAG)
    return tag.text.strip() if tag else None