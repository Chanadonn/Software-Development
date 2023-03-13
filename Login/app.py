import streamlit as st
from py_avataaars import PyAvataaar
from PIL import Image
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

with open('F:/NPO/Login/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

