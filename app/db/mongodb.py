from pymongo import MongoClient
from app.core.config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)

database = client[DB_NAME] # type: ignore

blog_collection = database["blogs"]