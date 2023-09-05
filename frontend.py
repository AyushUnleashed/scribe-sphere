import streamlit as st
import time

# Function to simulate generating an email
from generate_email import generate_email

# Streamlit app title
st.title("Scribe-Sphere")
st.subheader("Your Personalised cold email writer")

# Text field for pasting company information
company_info = st.text_area("Paste Company Information Here:")

# Initialize a variable to store the generated email
generated_email = None

# Button to generate email
if st.button("Generate Email", key="generate_button", disabled=False):
    # # Disable the button to prevent multiple clicks
    # st.button("Generate Email", key="generate_button", disabled=True)

    # Display a loading message while waiting for the function to finish
    loading_text = st.text("Generating email, please wait...")

    # Call the function to generate the email
    generated_email = generate_email(company_info)

    # Remove the loading message and enable the button again
    loading_text.empty()
    # st.button("Generate Email", key="generate_button", disabled=False)

# Display the generated email if available
if generated_email:
    st.header("Generated Email:")
    st.write(generated_email)