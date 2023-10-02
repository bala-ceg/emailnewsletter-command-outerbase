import streamlit as st
import re
import requests

st.title("Newsletter Signup")


email = st.text_input("Enter your email")
name = st.text_input("Enter your name")
gdpr_consent = st.checkbox("I agree to the privacy policy")


def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email)


if st.button("Subscribe"):
    if not gdpr_consent:
        st.error("You must agree to the privacy policy to subscribe.")
    elif not is_valid_email(email):
        st.error("Please enter a valid email address.")
    else:
        data = {
            "email": email,
            "name": name,
        }
        url = "https://arbitrary-fuchsia.cmd.outerbase.io/confirm_signup"

        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                st.success(f"Thank you, {name}! You have successfully subscribed to our newsletter with email: {email}")
            else:
                st.error("Failed to subscribe. Please try again later.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
