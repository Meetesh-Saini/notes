import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.wow
logins = db["admin"]

with open("users.json") as f:
    users = json.load(f)

logins.insert_many(users)
