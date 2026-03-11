"""
CRUD (Create, Read, Update, Delete) operations for blog posts.
Contains all database operations logic.
"""

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from app.db.mongodb import blog_collection
from app.schemas.serializeObjects import serializeDict, serializeList
from app.models.blog_model import CreateBlog, UpdateBlog


def create_blog(blog_data: CreateBlog):
    """
    Called on post route | get blog creation data | insert into mongodb
    """
    try:
        result = blog_collection.insert_one(blog_data.model_dump())

        blog = blog_collection.find_one({"_id": ObjectId(result.inserted_id)})

        if blog is None:
            raise HTTPException(status_code=500, detail="Blog creation failed")

        return serializeDict(blog)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating blog: {str(e)}")


def get_all_blogs():
    """
    Retrieves all blogs from mongodb
    """
    try:
        blogs = blog_collection.find()
        return serializeList(blogs)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


def get_blog_by_id(id: str):
    """
    Finds Blog in mongodb via id | return data if found else error
    """
    try:
        blog = blog_collection.find_one({"_id": ObjectId(id)})

        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        return serializeDict(blog)

    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid blog ID")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


def update_blog(id: str, blog_data: UpdateBlog):
    """
    Called on PUT route | get blog updation data | updates into mongodb
    """
    try:
        updated = blog_collection.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": blog_data.model_dump(exclude_unset=True)}
        )

        if updated is None:
            raise HTTPException(status_code=404, detail="Blog not found")

        updated_blog = blog_collection.find_one({"_id": ObjectId(id)})
        return serializeDict(updated_blog)

    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid blog ID")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating blog: {str(e)}")
