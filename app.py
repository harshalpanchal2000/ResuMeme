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
    auth_url = f"{authorization_url}?{urlencode(params)}"

    # Display authorization URL
    st.write("Authorization URL:", auth_url)

    # You can redirect the user to this URL for authorization
    # You'll need to handle the authorization code returned from Indeed
    # and exchange it for an access token using the code verifier

if __name__ == "__main__":
    main()
