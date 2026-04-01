from app.core.config import URL
import requests

url = URL or None
headers = {"User-Agent": "Mozilla/5.0"}


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
