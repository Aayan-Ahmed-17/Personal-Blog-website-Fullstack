from app.services.parse import parse_data
from app.services.scrape import get_data, url, headers
from fastapi import FastAPI

app = FastAPI()


@app.get("/blogs")
def read_blogs():
    response = get_data(url=url, headers=headers)
    return parse_data(response)
