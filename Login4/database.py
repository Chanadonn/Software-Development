import os
from deta import Deta
from dotenv import load_dotenv
import hashlib

load_dotenv(".env")

DETA_KEY = os.getenv("DETA_KEY")

deta = Deta(DETA_KEY)

db = deta.Base("users_db")

def insert_user(username, name, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return db.put({"key": username, "name": name, "password": hashed_password})

def fetch_all_users():
    res = db.fetch()
    return res.items

def get_user(username):
    return db.get(username)

def update_user(username, updates):
    return db.update(updates, username)

def delete_user(username):
    return db.delete(username)

def authenticate_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = get_user(username)
    if user and user["password"] == hashed_password:
        return user["name"]
    else:
        return None

#insert_user("one","one","111")
#delete_user("One")