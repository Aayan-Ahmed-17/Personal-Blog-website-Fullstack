from app.services.scraper.scrape import get_data, headers, url
from bs4 import BeautifulSoup

blog_grid_container_select = "div.grid.w-full.grid-cols-1.gap-4.p-2"
blog_container_select = "div.p-6.bg-white.rounded-xl"
blog_link_select = "div a"
blog_img_link_select = "div a div img"
blog_title_select = "div a h3"
blog_update_data_select = "div div div span.text-gray-500"
blog_description_select = "div div p.mt-6.leading-normal.text-gray-600.line-clamp-3"


def parse_data(response):
    try:
        soup = BeautifulSoup(response.content, "html.parser")

        blog_grid_container = soup.select_one(blog_grid_container_select)
        if not blog_grid_container:
            print("Blog grid container not found — selector may be outdated")
            return None

        # print(blog_grid_container.prettify())  # Debug: print the blog grid container HTML
        
        blog_containers = blog_grid_container.select(blog_container_select) # type: ignore
        for i, blog in enumerate(blog_containers):
            blog_link = blog.select_one(blog_link_select)
            img_tag = blog.select_one(blog_img_link_select)
            title_tag = blog.select_one(blog_title_select)
            date_tags = blog.select(blog_update_data_select)
            description_tag = blog.select_one(blog_description_select)

        # Validate before extracting
        # if not blog_link:
        #     print("Blog link not found")
        #     return None
        # if not img_tag:
        #     print("Image tag not found")
        #     return None
        # if not title_tag:
        #     print("Title tag not found")
        #     return None
        # if len(date_tags) < 4:
        #     print(f"Expected 4+ date spans, found {len(date_tags)}")
        #     return None
        # if not description_tag:
        #     print("Description tag not found")
        #     return None

        return {
            "blog_containers": len(blog_containers),
            # "blog_link": blog_link.get("href"),
            # "img_link": img_tag.get("src"),
            # "title": title_tag.text.strip(),
            # "latest_date": date_tags[1].text.strip(),
            # "description": description_tag.text.strip(),
        }

    except Exception as e:
        print(f"Unexpected error during parsing: {e}")
        return None


response = get_data(url=url, headers=headers)
parse_data(response)

# if response:
#     result = parse_data(response)
#     if result:
#         for key, value in result.items():
#             print(f"{key}: {value}")
