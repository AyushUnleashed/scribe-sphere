import streamlit as st
import os
from resume_to_text import convert_pdf_to_text
# Function to simulate generating an email
from generate_email import generate_email

# Streamlit app title
st.title("Scribe-Sphere")
st.subheader("Your Personalized cold email writer")

# Function to validate email
def is_valid_email(email):
    # You can implement your email validation logic here
    # For a simple check, we'll just ensure it contains '@'
    return '@' in email

# Function to check if resume exists
def does_resume_exist(email_id):
    resume_path = os.path.join('generations', f"{email_id}_resume.pdf")
    return os.path.isfile(resume_path)

# Ask for user's email ID
email_id = st.text_input("Enter your Email ID:")
if email_id:
    if is_valid_email(email_id):
        st.success("Valid email ID entered.")
        resume_exists = does_resume_exist(email_id)

        # Check if the resume exists or the user has uploaded one
        if not resume_exists:
            uploaded_file = st.file_uploader("Upload your PDF resume:")

            if uploaded_file is not None:
                resume_path = os.path.join('generations', f"{email_id}_resume.pdf")
                with open(resume_path, "wb") as f:
                    f.write(uploaded_file.read())

                st.success("Resume uploaded and saved successfully.")

                # Call a function to convert PDF to text
                text_resume = convert_pdf_to_text(resume_path)
                # You can use 'text_resume' for further processing

        # Only if the resume exists or has been uploaded, proceed with company information input
        if resume_exists or uploaded_file is not None:
            company_info = ""
            company_name = ""
            # Radio button to choose whether to input company name or company information
            selection = st.radio("Choose Input Option:", ("Company Name", "Company Information"))

            # Text field for pasting company information
            if selection == "Company Information":
                company_info = st.text_area("Paste Company Information Here:")

            # Text field for entering the company name
            if selection == "Company Name":
                company_name = st.text_input("Enter Company Name:")

            # Initialize a variable to store the generated email
            generated_email = None

            # Button to generate email
            if st.button("Generate Email", key="generate_button", disabled=False):
                if not company_info and not company_name:
                    st.warning("Please fill in at least one field (Company Name or Company Information).")
                else:
                    # Display a loading message while waiting for the function to finish
                    loading_text = st.text("Generating email, please wait...")

                    if selection == "Company Information":
                        # Call the function to generate the email with company information
                        generated_email = generate_email(email_id, company_info, "",)
                    elif selection == "Company Name":
                        # Call the function to generate the email with company name
                        generated_email = generate_email(email_id,"", company_name)

                    # Remove the loading message and enable the button again
                    loading_text.empty()

            # Display the generated email if available
            if generated_email:
                st.header("Generated Email:")
                st.write(generated_email)

    else:
        st.warning("Please enter a valid email ID.")