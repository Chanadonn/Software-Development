import streamlit as st
#import pickle
#from pathlib import Path
import streamlit_authenticator as stauth
import database as db

users = db.fetch_all_users()

usernames        = [user["key"] for user in users]
names            = [user["name"] for user in users]
hashed_passwords = [user["password"] for user in users]

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    'test', 'abcdef', cookie_expiry_days=30)

name, authentication_status = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("logout","sidebar")
    st.sidebar.title(f"Welcome {name}")