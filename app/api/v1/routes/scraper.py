from app.services.scraper.parse import parse_all_blogs, fetch_response
from app.services.scraper.scrape import get_data, url, headers
from fastapi import APIRouter

router = APIRouter(
    prefix="/scraped",  # All paths in this router will start with "/scraped"
    tags=["scraped"],  # Adds a tag for documentation in /docs
)

"""
POST /api/scraped/fetch: Trigger a scraper (takes URL, returns content). WILL IMPLEMENT LATER
GET /api/scraped/: Retrieve all saved scraped articles.
GET /api/scraped/{id}: Read a specific scraped article.
DELETE /api/scraped/{id}: Delete a specific scraped article.
"""


@router.get("/")
def read_blogs():
    """Fetch and parse blogs on demand"""
    try:
        response = fetch_response()
        if response is None:
            return {"error": "Could not fetch data from URL"}
        blogs = parse_all_blogs(response)
        return blogs
    except Exception as e:
        return {"error": f"Failed to parse blogs: {str(e)}"}


@router.get("/{id}")
def read_blog(id: str):
    """Retrieves a specific scraped article by its ID."""
    return {"message": f"Retrieving scraped article with ID: {id}"}


@router.delete("/{id}")
def delete_blog(id: str):
    """Deletes a specific scraped article by its ID."""
    return {"message": f"Deleting scraped article with ID: {id}"}
