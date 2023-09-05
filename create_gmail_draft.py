import os
import base64
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Load the credentials JSON file
credentials_file = 'your-credentials.json'
credentials = service_account.Credentials.from_service_account_file(
    credentials_file, scopes=['https://www.googleapis.com/auth/gmail.compose']
)

# Create a Gmail API service instance
service = build('gmail', 'v1', credentials=credentials)

# Function to create a draft with the given subject, content, and recipient
def create_draft(subject, content, recipient_email):
    message = {
        'raw': base64.urlsafe_b64encode(
            f"Subject: {subject}\nTo: {recipient_email}\n\n{content}".encode('utf-8')
        ).decode('utf-8')
    }
    try:
        draft = service.users().drafts().create(userId='me', body=message).execute()
        return draft
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# # Read text from a file
# file_path = 'your-file.txt'
# with open(file_path, 'r', encoding='utf-8') as file:
#     text_content = file.read()
#
# # Set the recipient's email address
# recipient_email = 'recipient@example.com'  # Replace with the recipient's email address
#
# # Create a draft with the text content and recipient
# draft_subject = 'Your Subject'
# draft = create_draft(draft_subject, text_content, recipient_email)
#

def save_draft(draft_subject,text_content,recipient_email):
    draft = create_draft(draft_subject, text_content, recipient_email)
    if draft:
        print(f"Draft '{draft_subject}' created successfully.")
