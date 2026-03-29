import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME", "")
PASSWORD = os.getenv("PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "blog_fullstack")

# Build MONGO_URI with SSL certificate workaround
if USERNAME and PASSWORD:
    MONGO_URI = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.r2krjac.mongodb.net/{DB_NAME}?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
    print("✓ MONGO_URI successfully constructed.")
else:
    raise ValueError("❌ ERROR: USERNAME or PASSWORD not found in .env file")