import streamlit as st
from urllib.parse import urlencode

# Function to authenticate with Indeed API using OAuth
def authenticate():
    # Indeed OAuth authorization URL
    oauth_url = "https://secure.indeed.com/account/login/oauth2/auth"

    # OAuth client credentials (replace with your credentials)
    client_id = "e5b55c005f62d4c5c32ae11ed9a0df3c132d94b2627d2dc9bcf473823fcd1022"
    redirect_uri = "https://ca.indeed.com/"  # Redirect URI registered with Indeed
    scope = "apply"  # Scopes required by your application

    # Construct OAuth authorization URL
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": scope,
        "response_type": "code"
    }
    authorization_url = f"{oauth_url}?{urlencode(params)}"

    # Redirect user to OAuth authorization URL
    st.markdown(f"Click [here]({authorization_url}) to authenticate with Indeed.")

# Set page configuration
st.set_page_config(page_title="ResumeMe", page_icon=":briefcase:", layout="wide")

# Main Streamlit UI
def main():
    st.title("ResumeMe: Your Job Application Assistant")
    st.subheader("Automate your job application process with ease!")

    # Authentication
    authenticate()

# Run the app
if __name__ == "__main__":
    main()
