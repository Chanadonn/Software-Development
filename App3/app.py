"""
import streamlit as st
import bcrypt
import database as db
import avatar
from streamlit.caching.hashing import _CacheFuncHasher
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server
from typing import Dict

"""
# --- USER AUTHENTICATION ---
"""

# Get usernames and hashed passwords from the database
users = db.fetch_all_users()
usernames = [user["key"] for user in users]
hashed_passwords = [user["password"] for user in users]

# Define the login function
def login():
    session_state = get_session()
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in usernames:
            user_index = usernames.index(username)
            hashed_password = hashed_passwords[user_index].encode("utf-8")
            if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
                session_state.logged_in = True
                session_state.username = username
                st.sidebar.success("Logged in as {}".format(username))
                return True
            else:
                st.sidebar.error("Incorrect password")
        else:
            st.sidebar.error("Username not found")
    return False

# Define the logout function
def logout():
    session_state = get_session()
    session_state.logged_in = False
    st.sidebar.button("Logout")

# Define the session state
def get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id).session
    if not hasattr(session_info, "custom_session_state"):
        session_info.custom_session_state = {}
    return session_info.custom_session_state

# Test the login function
session_state = get_session()
if "logged_in" not in session_state:
    session_state.logged_in = False

if session_state.logged_in:
    st.title("Welcome to the app!")
    avatar()
    logout()
else:
    st.warning("Please log in.")
    login()
"""
import streamlit as st
import bcrypt
import database as db
import avatar

"""
# --- USER AUTHENTICATION ---
"""

# Get usernames and hashed passwords from the database
users = db.fetch_all_users()
usernames = [user["key"] for user in users]
hashed_passwords = [user["password"] for user in users]

# Define the login function
def login():
    session_state = get_session()
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in usernames:
            user_index = usernames.index(username)
            hashed_password = hashed_passwords[user_index].encode("utf-8")
            if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
                session_state.logged_in = True
                session_state.username = username
                st.sidebar.success("Logged in as {}".format(username))
                return True
            else:
                st.sidebar.error("Incorrect password")
        else:
            st.sidebar.error("Username not found")
    return False

# Define the logout function
def logout():
    session_state = get_session()
    session_state.logged_in = False
    st.sidebar.button("Logout")
    st.warning("Please log in.")

# Define the session state
def get_session():
    session_state = st.session_state
    if "logged_in" not in session_state:
        session_state.logged_in = False
    return session_state


# Test the login function
session_state = get_session()
if session_state.logged_in:
    st.title("Welcome to the app!")
    avatar()
    logout()
else:
    st.warning("Please log in.")
    login()
