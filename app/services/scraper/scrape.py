import os
from dotenv import load_dotenv
import requests

load_dotenv()

# get env variables
url = os.getenv("URL")
custom_user_agent = os.getenv("USER_AGENT")

headers = {
    'User-Agent': custom_user_agent or 'Mozilla/5.0'
}

# Don't raise error at import time - will handle in the route
# if not url:
#     raise ValueError("URL not found in .env file")

def get_data(url, headers=None):
    """Fetch data from URL"""
    if not url:
        return None
        
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error {e.response.status_code}: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return None
