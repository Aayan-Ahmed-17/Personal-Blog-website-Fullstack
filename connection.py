from pymongo import MongoClient  # type: ignore
from dotenv import load_dotenv
import os

# load environment variable from .env file
load_dotenv()
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DB")
COLLECTION = os.getenv("COLLECTION")

# Mongodb connection URI
uri = f"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster0.r2krjac.mongodb.net/"

def get_db():
    MONGO_URI = os.getenv('MONGO_URI')
    client = MongoClient(MONGO_URI)
    db = client['mydatabase']
    print("Connected to MongoDB")
    return db

get_db()