from scrape import get_data, headers, url
from bs4 import BeautifulSoup

response = get_data(url=url, headers=headers)

blog_container_classes = "div.grid.w-full.grid-cols-1.gap-4.p-2"
item_card_classes = "div.p-6.bg-white.rounded-xl"

container = None

"""
===========desired extract content==============
blog_link
img_link
title
latest date
description
"""


def parse_data():
    try:
        soup = BeautifulSoup(response.content, "html.parser")  # type: ignore
        container = soup.select_one(blog_container_classes)

    except Exception as e:
        print(f"Error: {e}")
