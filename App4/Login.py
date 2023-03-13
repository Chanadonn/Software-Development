import yaml
import streamlit as st
from streamlit_authenticator import Authenticate

# Load YAML file
with open('config.yaml') as file:
    config = yaml.safe_load(file)

# Create instance of Authenticate class
authenticator = Authenticate(
    config['credentials']['usernames'],
    config['credentials']['cookie']['name'],
    config['credentials']['cookie']['key'],
    config['credentials']['cookie']['expiry_days'],
    config['credentials']['preauthorized']
)

if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

# Create login page and retrieve username and authentication status
name, authentication_status, username = authenticator.login('Login')


# Display appropriate message based on authentication status
if authentication_status:
    st.write(f'Welcome {name}!')
    # Add your content here
else:
    st.error('Username/password is incorrect')

# Create logout button
authenticator.logout('Logout', 'My Login Page')
