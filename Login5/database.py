import os 
from deta import Deta
from dotenv import load_dotenv
#import hashlib

load_dotenv(".env")

DETA_KEY = os.getenv("DETA_KEY")

deta = Deta(DETA_KEY)

db = deta.Base("Login_data")

def fetch_all_users():
    res = db.fetch()
    return res.items

def insert_user(username , name , password):
    #hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return db.put({"key": username , "name" : name , "password" : password})

def update_user(username , updates):
    return db.update(username , updates)

def delete_user(username):
    return db.delete(username)

def get_user(username):
    return db.get(username)
"""
def authenticate_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = get_user(username)
    if user and user["password"] == hashed_password:
        return user["name"]
    else:
        return None
"""
#insert_user("Test4" , "No.4" , "654")
#delete_user("Test4")
