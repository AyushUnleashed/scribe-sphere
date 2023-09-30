import requests
from bs4 import BeautifulSoup

# Function to scrape HTML content from a webpage
def scrape_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error scraping webpage: {e}")
        return None

# Function to find and print input fields and their identifiers
def find_input_fields(html_content):
    if not html_content:
        return

    soup = BeautifulSoup(html_content, 'html.parser')

    input_fields = {}

    # Find input fields with various types (text, file, checkbox, radio, select)
    for input_tag in soup.find_all(['input', 'textarea', 'select']):
        field_name = input_tag.get('name') or input_tag.get('id') or input_tag.get('placeholder') or input_tag.get('title') or 'Unnamed Field'
        input_fields[field_name] = input_tag.get('id') or input_tag.get('name') or input_tag.get('class') or input_tag.get('placeholder') or input_tag.get('title') or 'No Identifier'

    # Print the key-value pairs
    for key, value in input_fields.items():
        print(f"Field Name: {key}")
        print(f"HTML Identifier: {value}")
        print()

if __name__ == "__main__":
    # Replace 'your_website_url_here' with the URL of the webpage you want to scrape
    website_url = 'https://jobs.lever.co/helpshift/8d161cab-a9dc-44be-acd2-e02c087c05c3/apply'

    # Scrape the webpage
    html_content = scrape_webpage(website_url)

    if html_content:
        # Find and print input fields
        find_input_fields(html_content)