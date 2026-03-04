import os
from dotenv import load_dotenv
import requests

load_dotenv()

# get env variables
url = os.getenv("URL")
custom_user_agent = os.getenv("USER_AGENT")

headers = {
    'User-Agent': custom_user_agent
}

if not url:
    raise ValueError("URL not found in .env file")

def get_data(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error {e.response.status_code}: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return None
