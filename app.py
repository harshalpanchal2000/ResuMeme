import streamlit as st
import requests
from urllib.parse import urlencode
from hashlib import sha256
from base64 import urlsafe_b64encode
import secrets

# Function to generate code verifier and code challenge
def generate_code_verifier_and_challenge():
    code_verifier = secrets.token_urlsafe(100)
    code_challenge = urlsafe_b64encode(sha256(code_verifier.encode()).digest()).rstrip(b'=')
    return code_verifier, code_challenge

# Streamlit app
def main():
    st.title("Resumeme - Indeed OAuth")
    st.subheader("Connect your Resumeme account with Indeed")

    # Replace with your client ID and redirect URI
    client_id = "e5b55c005f62d4c5c32ae11ed9a0df3c132d94b2627d2dc9bcf473823fcd1022"
    redirect_uri = "https://ca.indeed.com/"

    # Generate code verifier and challenge
    code_verifier, code_challenge = generate_code_verifier_and_challenge()

    # Build authorization URL with PKCE parameters
    authorization_url = "https://secure.indeed.com/oauth/v2/authorize"
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "code_challenge": code_challenge.decode(),
        "code_challenge_method": "S256"  # SHA256 method
    }
    auth_url = f"[Authorize Resumeme to access your Indeed account]({authorization_url}?{urlencode(params)})"

    # Display link to authorize Resumeme
    st.markdown(auth_url, unsafe_allow_html=True)

    # Capture user input for desired position and location
    position = st.text_input("Enter the desired position:", "")
    location = st.text_input("Enter the desired location:", "")

    # Button to submit the search
    if st.button("Search"):
        # Perform search with the provided position and location
        st.write("Performing search for position:", position, "in location:", location)

if __name__ == "__main__":
    main()
