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

client = MongoClient(uri)
db = client[DB]
collection = db[COLLECTION]

print("connected successfully")

