from app.db.mongodb import blog_collection


def create_blog(blog_data: dict):
    result = blog_collection.insert_one(blog_data)
    return str(result.inserted_id)
