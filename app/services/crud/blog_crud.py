from app.db.mongodb import blog_collection
from app.utils.serializer import blog_serializer


def create_blog(blog_data: dict):
    result = blog_collection.insert_one(blog_data)
    return str(result.inserted_id)


def get_all_blogs():
    blogs = blog_collection.find()
    return [blog_serializer(blog) for blog in blogs]


def get_blog(blog_id):
    blog = blog_collection.find_one({"_id": blog_id})
    return blog_serializer(blog)