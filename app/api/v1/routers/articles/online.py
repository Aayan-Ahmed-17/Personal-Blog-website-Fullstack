from app.services.scraper.parse import parse_all_blogs, response
from app.services.scraper.scrape import get_data, url, headers
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_blogs():
    blogs = parse_all_blogs(response)
    return blogs

