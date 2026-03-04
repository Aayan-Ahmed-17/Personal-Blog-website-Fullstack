from app.services.scraper.parse import parse_data
from app.services.scraper.scrape import get_data, url, headers
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_blogs():
    response = get_data(url=url, headers=headers)
    return parse_data(response)

