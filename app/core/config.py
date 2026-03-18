import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME", "")
PASSWORD = os.getenv("PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "blog_fullstack")

# Build MONGO_URI with error handling
if USERNAME and PASSWORD:
    MONGO_URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.r2krjac.mongodb.net/"
else:
    MONGO_URI = None  # Will be set later or raise error