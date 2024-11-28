from flask import Flask, Response, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.test
logins = db["a"]
FLAG = "ctf{!nj3cti0n_hurt$}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=("POST",))
def login():
    query = request.get_json(force=True)
    print(query)
    cur = logins.find_one({
        "user" : query["username"],
        "passwd" : query["password"]
        })
    if cur:
        return f"Exploit successful: {FLAG}"
    return Response(status=400)

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
