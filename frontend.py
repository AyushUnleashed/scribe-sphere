import streamlit as st
import time

# Function to simulate generating an email
from generate_email import generate_email

# Streamlit app title
st.title("Scribe-Sphere")
st.subheader("Your Personalized cold email writer")

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
            generated_email = generate_email(company_info, "")
        elif selection == "Company Name":
            # Call the function to generate the email with company name
            generated_email = generate_email("", company_name)

        # Remove the loading message and enable the button again
        loading_text.empty()

# Display the generated email if available
if generated_email:
    st.header("Generated Email:")
    st.write(generated_email)