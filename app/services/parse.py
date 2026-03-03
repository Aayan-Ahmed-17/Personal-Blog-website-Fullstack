from app.services.scrape import get_data, headers, url
from bs4 import BeautifulSoup

blog_container_select = "div.grid.w-full.grid-cols-1.gap-4.p-2"
blog_link_select = "div a"
blog_img_link_select = "div a div img"
blog_title_select = 'div a h3'
blog_update_data_select = 'div div div span.text-gray-500'
blog_description_select = 'div div p.mt-6.leading-normal.text-gray-600.line-clamp-3'


def parse_data(response):
    try:
        soup = BeautifulSoup(response.content, "html.parser")

        blog_container = soup.select_one(blog_container_select)
        if not blog_container:
            print("Blog container not found — selector may be outdated")
            return None

        blog_link = blog_container.select_one(blog_link_select)
        img_tag = blog_container.select_one(blog_img_link_select)
        title_tag = blog_container.select_one(blog_title_select)
        date_tags = blog_container.select(blog_update_data_select)
        description_tag = blog_container.select_one(blog_description_select)

        # Validate before extracting
        if not blog_link:
            print("Blog link not found")
            return None
        if not img_tag:
            print("Image tag not found")
            return None
        if not title_tag:
            print("Title tag not found")
            return None
        if len(date_tags) < 4:
            print(f"Expected 4+ date spans, found {len(date_tags)}")
            return None
        if not description_tag:
            print("Description tag not found")
            return None

        return {
            "blog_link":        blog_link.get("href"),
            "img_link":         img_tag.get("src"),
            "title":            title_tag.text.strip(),
            "latest_date":      date_tags[1].text.strip(),
            "description":      description_tag.text.strip(),
        }

    except Exception as e:
        print(f"Unexpected error during parsing: {e}")
        return None


response = get_data(url=url, headers=headers)

# if response:
#     result = parse_data(response)
#     if result:
#         for key, value in result.items():
#             print(f"{key}: {value}")