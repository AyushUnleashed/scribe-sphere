import os
import base64
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Load the credentials JSON file
def load_credentials(credentials_file):
    try:
        credentials = service_account.Credentials.from_service_account_file(
            credentials_file, scopes=['https://www.googleapis.com/auth/gmail.compose']
        )
        return credentials
    except FileNotFoundError:
        print(f"Error: {credentials_file} not found.")
        return None

# Create a Gmail API service instance
def create_gmail_service(credentials):
    if credentials:
        service = build('gmail', 'v1', credentials=credentials)
        return service
    else:
        return None

# Function to create a draft with the given subject, content, and recipient
def create_draft(service, subject, content, recipient_email):
    if not service:
        return None
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

# Read text from a file
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

# Main function to orchestrate the process
def create_gmail_draft(credentials_file, file_path, recipient_email, draft_subject):
    credentials = load_credentials(credentials_file)
    service = create_gmail_service(credentials)

    if not service:
        print("Gmail service not available. Exiting.")
        return

    text_content = read_text_from_file(file_path)

    if text_content is not None:
        draft = create_draft(service, draft_subject, text_content, recipient_email)

        if draft:
            print(f"Draft '{draft_subject}' created successfully.")

if __name__ == "__main__":
    credentials_file = '../client_secrets_scribe_sphere.json'
    file_path = 'generations/generated_email.txt'
    recipient_email = 'recipient@example.com'  # Replace with the recipient's email address
    draft_subject = 'Internship Want'

    create_gmail_draft(credentials_file, file_path, recipient_email, draft_subject)