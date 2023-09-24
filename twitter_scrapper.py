import requests
from bs4 import BeautifulSoup

def scrape_twitter_thread(thread_url):
    try:
        # Send an HTTP GET request to the Twitter thread URL
        response = requests.get(thread_url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and print all elements with the specified classes
        elements_with_classes = soup.find_all(class_=lambda x: x and 'css-901oao' in x and 'css-16my406' in x and 'r-poiln3' in x and 'r-bcqeeo' in x and 'r-qvutc0' in x)
        for element in elements_with_classes:
            print(element.get_text())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# Example usage
thread_url = 'https://twitter.com/AviSchiffmann/status/1701065176785854840'
scrape_twitter_thread(thread_url)