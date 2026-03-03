from scrape import get_data, headers, url
from bs4 import BeautifulSoup

response = get_data(url=url, headers=headers)

blog_container_select = "div.grid.w-full.grid-cols-1.gap-4.p-2"
item_card_select = "div.p-6.bg-white.rounded-xl"
blog_link_select = "div a"
blog_img_link_select = "div a div img"
blog_title_select = 'div a h3'
blog_update_data_select = 'div div div span'

container = None

"""
===========desired extract content==============
blog_link
img_link
title
latest date
description
"""


# def parse_data():
#     try:
soup = BeautifulSoup(response.content, "html.parser")  # type: ignore
blog_container = soup.select_one(blog_container_select)
blog_link = blog_container.select_one(blog_link_select).get("href")  # type: ignore
img_link = blog_container.select_one(blog_img_link_select).get("src") # type: ignore
blog_title = blog_container.select_one(blog_title_select).text # type: ignore
blog_update_data = blog_container.select(blog_update_data_select)[3].text # type: ignore

        # print(blog)
    # except Exception as e:
    #     print(f"Error: {e}")
