import base64
from email.message import EmailMessage
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def create_service(credentials):
    service = build('gmail', 'v1', credentials=credentials)
    return service


def create_send_email_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(error)


def create_draft_email_message(sender, to, subject, message_text, attachments: list = None):
    message = EmailMessage()
    message.set_content(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    # attachments
    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as content_file:
                content = content_file.read()
                message.add_attachment(content, maintype='application', subtype=(attachment.split('.')[1]),
                                       filename=attachment)

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {
        'message': {
            'raw': encoded_message
        }
    }
    return create_message


def draft_message(service, user_id, message):
    try:
        draft = (service.users().drafts().create(userId=user_id, body=message).execute())
        print('Draft Id: %s' % draft['id'])

    except HttpError as error:
        print(F'An error occurred: {error}')
        draft = None

    return draft


def get_service():
    # Get credentials
    credentials = get_credentials()

    if not credentials:
        print("Credentials not available. Exiting.")
        return

    # Create Gmail service
    service = create_service(credentials)
    return service


from google_auth import get_credentials


def send_draft_email(to, subject, message_text):
    from_user = 'me'
    service = get_service()
    # Create a message
    message = create_draft_email_message(from_user, to, subject, message_text)
    # Draft the message
    print(draft_message(service, user_id=from_user, message=message))


def main():
    send_draft_email('ayushyadavytube@gmail.com', 'Subject ', 'message ')


if __name__ == "__main__":
    main()
