import streamlit as st
import bcrypt
import database as db
#import avatar

"""
# --- USER AUTHENTICATION ---
"""

# Get usernames and hashed passwords from the database
users = db.fetch_all_users()
usernames = [user["key"] for user in users]
hashed_passwords = [user["password"] for user in users]

# Define the login function
def login():
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in usernames:
            user_index = usernames.index(username)
            hashed_password = hashed_passwords[user_index].encode("utf-8")
            if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
                st.sidebar.success("Logged in as {}".format(username))
                st.title("Welcome to the app!")
                import avatar
                avatar()
                return True
            else:
                st.sidebar.error("Incorrect password")
        else:
            st.sidebar.error("Username not found")
    return False

# Test the login function
if login():
    st.sidebar.button("Logout")
else:
    st.warning("Please log in.")
