import streamlit as st
import bcrypt
import database as db
#from streamlit.hashing import _CodeHasher
##from hasher import Hasher
#from streamlit.report_thread import REPORT_CONTEXT_ATTR_NAME
#from streamlit.server.Server import Server

##import functools
##import inspect

"""
# --- USER AUTHENTICATION ---
"""


# Get usernames and hashed passwords from the database
users = db.fetch_all_users()
usernames = [user["key"] for user in users]
hashed_passwords = [user["password"] for user in users]

# Create a SessionState object to store the login state
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

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

                import avatar
                avatar()
                if st.sidebar.button("Logout"):
                    state.logged_in = False
                return True
            else:
                st.sidebar.error("Incorrect password")
        else:
            st.sidebar.error("Username not found")
    return False

state = SessionState(logged_in=False)

# Check the login status and show appropriate content
if state.logged_in:
    st.title("Welcome to the app!")

else:
    if login():
        state.logged_in = True
        
    else:
        st.warning("Please log in.")
