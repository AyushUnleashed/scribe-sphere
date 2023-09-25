from generate_email import generate_email
from send_draft import send_draft_email
import os

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{file_path}' not found. Execution halted.")


def main():
    # Call generate_email to create the email content file
    generate_email()
    file_path = "generations/generated_email.txt"
    message_text = read_text_file(file_path)
    send_draft_email('ayushyadavytube@gmail.com','Internship Opportunity',message_text=message_text)

if __name__ == "__main__":
    main()