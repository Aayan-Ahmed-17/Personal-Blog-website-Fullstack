"""
CRUD (Create, Read, Update, Delete) operations for blog posts.
Contains all database operations logic.
"""
from bson import ObjectId
from app.db.mongodb import blog_collection
from app.schemas.serializeObjects import serializeDict, serializeList
from app.models.blog_model import BlogModel
# from app.utils.serializer import blog_serializer


# async def InsertUser(data: BlogModel):
#     result = blog_collection.insert_one(dict(data))
#     return serializeDict(blog_collection.find_one({"_id": ObjectId(result.inserted_id)}))

def create_blog(blog_data: BlogModel):
    try:
        result = blog_collection.insert_one(dict(blog_data))
        return serializeDict(blog_collection.find_one({"_id": ObjectId(result.inserted_id)}))
    except Exception as e:
            raise Exception(f"✗ Error creating blog: {str(e)}")
            


def get_all_blogs():
    blogs = blog_collection.find()
    return [blog_serializer(blog) for blog in blogs]


def get_blog(blog_id):
    blog = blog_collection.find_one({"_id": blog_id})
    return blog_serializer(blog)