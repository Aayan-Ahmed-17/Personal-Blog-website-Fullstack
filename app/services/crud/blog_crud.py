"""
CRUD (Create, Read, Update, Delete) operations for blog posts.
Contains all database operations logic.
"""

from bson import ObjectId
from app.db.mongodb import blog_collection
from app.schemas.serializeObjects import serializeDict, serializeList
from app.models.blog_model import CreateBlog, UpdateBlog


def create_blog(blog_data: CreateBlog):
    try:
        result = blog_collection.insert_one(dict(blog_data))
        return serializeDict(
            blog_collection.find_one({"_id": ObjectId(result.inserted_id)})
        )
    except Exception as e:
        raise Exception(f"✗ Error creating blog: {str(e)}")


def get_all_blogs():
    return serializeList(blog_collection.find())


def get_blog(id):
    return serializeDict(blog_collection.find_one({"_id": ObjectId(id)}))


def update_blog(id: str, blog_data: UpdateBlog):
    try:
        blog_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": blog_data.model_dump()},
        )

        updated_blog = blog_collection.find_one({"_id": ObjectId(id)})
        return serializeDict(updated_blog)

    except Exception as e:
        raise Exception(f"✗ Error updating blog: {str(e)}")
