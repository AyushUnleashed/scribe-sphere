from bs4 import BeautifulSoup
import requests
import os

def save_text_from_webpage(url, folder='generations'):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the text content from the parsed HTML
        text_content = soup.get_text()

        # Generate a filename based on the URL
        filename = os.path.join(folder, f'{url.replace("https://", "").replace("/", "_")}.txt')

        text_content = process_info(text_content)
        # Save the extracted text to the specified text file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text_content)
            # file.write("\n\nFiltered Emails:\n")
            # file.write("\n".join(filtered_emails))

        print(f'Text content saved to "{filename}"')
        return text_content
    else:
        print(f'Failed to retrieve webpage. Status code: {response.status_code}')


import re


def process_info(text_content: str) -> str:
    # Use regular expression to replace multiple consecutive empty lines with one empty line
    text_content = re.sub(r'\n\s*\n', '\n\n', text_content)

    return text_content


#
# def save_webpage(url, folder='generations'):
#     # Create the folder if it doesn't exist
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#
#     # Send an HTTP GET request to the URL
#     response = requests.get(url)
#
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the HTML content of the webpage
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # Generate a filename based on the URL
#         filename = os.path.join(folder, f'{url.replace("https://", "").replace("/", "_")}.html')
#
#         # Save the HTML to the specified file
#         with open(filename, 'w', encoding='utf-8') as file:
#             file.write(soup.prettify())
#
#         print(f'Webpage HTML saved to "{filename}"')
#     else:
#         print(f'Failed to retrieve webpage. Status code: {response.status_code}')

#
# def get_company_description(company_url):
#     try:
#         # Send an HTTP GET request to the company's website
#         response = requests.get(company_url)
#
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Parse the HTML content of the page using BeautifulSoup
#             soup = BeautifulSoup(response.text, 'html.parser')
#
#             # Depending on the structure of the website, you may need to inspect the HTML
#             # and identify the element containing the company description.
#             # Replace 'YOUR_CSS_SELECTOR' with the appropriate CSS selector for the description.
#             description_element = soup.select_one('YOUR_CSS_SELECTOR')
#
#             # Check if the description element was found
#             if description_element:
#                 # Extract the text from the element
#                 company_description = description_element.get_text()
#                 return company_description.strip()
#             else:
#                 return "Description not found on the webpage."
#
#         else:
#             return f"Failed to fetch the webpage (Status Code: {response.status_code})"
#
#     except Exception as e:
#         return f"An error occurred: {str(e)}"
