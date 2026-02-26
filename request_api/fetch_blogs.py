import requests

url = "https://books.toscrape.com/"

def scrape(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
if __name__ == "__main__":
    html_content = scrape(url)
    if html_content:
        print("Scraping successful!")
    else:
        print("Scraping failed.")