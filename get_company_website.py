import re

import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz  # Install the fuzzywuzzy library using pip

from urllib.parse import urlparse

def extract_tld_from_url(url):
    # Parse the URL to extract its components
    parsed_url = urlparse(url)

    # Split the hostname into parts
    hostname_parts = parsed_url.hostname.split('.')

    if len(hostname_parts) > 2:
        # If there are more than two parts, it likely has a subdomain
        tld = ".".join(hostname_parts[-2:])
        # Reconstruct the URL with the TLD
        result_url = f"{parsed_url.scheme}://{tld}{parsed_url.path}"
        return result_url
    else:
        return url  # No subdomain found, return the original U

def get_company_website(company_name):
    search_query = f"{company_name} official website"
    google_url = f"https://www.google.com/search?q={search_query}"

    try:
        response = requests.get(google_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('a')

            # Create a list to store the top 5 results
            top_results = []

            for link in search_results:
                href = link.get('href')
                if href.startswith('/url?q='):
                    website_link = href.replace('/url?q=', '').split('&')[0]

                    # Extract the link text and calculate similarity with the company name
                    link_text = link.get_text()
                    similarity_score = fuzz.ratio(company_name.lower(), link_text.lower())

                    top_results.append((website_link, similarity_score))

            # Sort the top results by similarity score in descending order
            top_results.sort(key=lambda x: x[1], reverse=True)

            # Return the link with the highest similarity score (top result)
            if top_results:
                return extract_tld_from_url(top_results[0][0])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return None

def get_website_by_company_name():
    company_name = "dusetch bak  "
    website = get_company_website(company_name)

    if website:
        print(f"The website of {company_name} is {website}")
    else:
        print(f"No website found for {company_name}")

if __name__ == "__main__":
    # Call the function to get the website link based on the company name
    get_website_by_company_name()