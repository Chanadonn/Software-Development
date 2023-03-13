import streamlit as st
from py_avataaars import PyAvataaar
from PIL import Image
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

#Page Set Up
st.set_page_config(page_title = "Project", page_icon = ":tada:", layout = "wide")

#Login
names = ["ONE", "TWO"]
usernames = ["one","two"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 
                                    "Project","abcdef", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Login","main")
"""
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.sidebar.title(f"Welcome {name}")
    st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
"""
if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Pls enter")

if authentication_status:
    #Content
    with st.container():
        st.title ("Character System")
        st.write ("CLASS: 6420301002")
    with st.container():
        avatar = PyAvataaar()
        avatar.render_png_file('avatar.png')
        image = Image.open('avatar.png')
        st.image(image)
    authenticator.logout("Logout","sidebar")

