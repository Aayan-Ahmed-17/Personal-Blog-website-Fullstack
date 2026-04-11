from pymongo import MongoClient
from app.core.config import MONGO_URI, DB_NAME

# Initialize as None, will be created on first use
client = None
database = None
blog_collection = None

def get_db():
    """Get or create database connection"""
    global client, database, blog_collection
    
    if client is None:
        if not MONGO_URI:
            raise ValueError("MONGO_URI is not configured. Please set USERNAME and PASSWORD env variables.")
        
        client = MongoClient(MONGO_URI)
        database = client[DB_NAME]
        blog_collection = database["blogs"]
    
    return database, blog_collection

# Try to initialize on import, but don't fail if unavailable
try:
    get_db()
except Exception as e:
    print(f"Warning: Could not initialize MongoDB on startup: {e}")
    print("Database will be initialized on first request.")