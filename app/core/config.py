import os
from dotenv import load_dotenv

load_dotenv(override=True)

USERNAME = os.getenv("USERNAME", "")
PASSWORD = os.getenv("PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "blog_fullstack")
URL = os.getenv("URL")

# Build MONGO_URI with SSL certificate workaround
if USERNAME and PASSWORD:
    MONGO_URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.r2krjac.mongodb.net/?appName=Cluster0"
    print("✓ MONGO_URI successfully constructed.", MONGO_URI)
else:
    raise ValueError("❌ ERROR: USERNAME or PASSWORD not found in .env file")
