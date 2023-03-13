import pickle
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth


st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


# USER AUTHENTICATION
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 
                                    "Project","abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    # SIDEBAR
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")

    # HIDE STREAMLIT STYLE
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)