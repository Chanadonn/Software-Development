import streamlit as st
import datetime as dt
import time
import bcrypt
import database as db

"""
# --- USER AUTHENTICATION ---
"""

# Get usernames and hashed passwords from the database
users = db.fetch_all_users()
usernames = [user["key"] for user in users]
hashed_passwords = [user["password"] for user in users]

# Create a SessionState object to store the login state and last login time
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def get_user_info(username):
    user_info = db.fetch_user(username)
    return user_info["last_login"], user_info["daily_login"]

state = SessionState(logged_in=False, last_login=None, daily_login=False)

# Define the login function
def login():
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in usernames:
            user_index = usernames.index(username)
            hashed_password = hashed_passwords[user_index].encode("utf-8")
            if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
                st.sidebar.success("Logged in as {}".format(username))
                state.logged_in = True
                state.last_login, state.daily_login = get_user_info(username)
                return True
            else:
                st.sidebar.error("Incorrect password")
        else:
            st.sidebar.error("Username not found")
    return False

# Check the login status and show appropriate content
if state.logged_in:
    st.title("Welcome to the app!")
    if state.daily_login:
        st.success("You received a point for logging in today!")
    else:
        st.warning("You did not log in yesterday. Please log in to receive your daily point.")
    if st.button("Logout"):
        db.update_user(state.last_login, state.daily_login, usernames[usernames.index(usernames)])
        state.logged_in = False
        state.last_login = None
        state.daily_login = False
else:
    if login():
        if st.sidebar.button("Logout"):
            db.update_user(state.last_login, state.daily_login, usernames[usernames.index(usernames)])
            state.logged_in = False
            state.last_login = None
            state.daily_login = False

        if state.daily_login:
            st.success("You received a point for logging in today!")
        elif state.last_login is not None:
            time_since_last_login = (dt.datetime.now() - state.last_login).total_seconds() / 3600
            if time_since_last_login >= 24:
                state.daily_login = True
        else:
            st.warning("You did not log in yesterday. Please log in to receive your daily point.")
            state.daily_login = True
        state.logged_in = True
        state.last_login = dt.datetime.now()
        db.update_user(state.last_login, state.daily_login, usernames[usernames.index(usernames)])
    else:
        st.warning("Please log in.")
