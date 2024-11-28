import os
from flask import Flask, Response, redirect, render_template, request, url_for, make_response
from pymongo import MongoClient
from itsdangerous import URLSafeTimedSerializer as Serializer, BadSignature, SignatureExpired

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["FLASK_KEY"]

client = MongoClient('localhost', 27017)
db = client.wow
logins = db["admin"]
FLAG = "ctf{!nj3cti0n_hurt$_t0o_mUCh}"
USER = "Cynthia"
PASSWD = logins.find_one({"user" : USER})["passwd"]
serializer = Serializer(app.config['SECRET_KEY'])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=("POST",))
def login():
    query = request.get_json(force=True)
    cur = logins.find_one({
        "user" : query["username"],
        "passwd" : query["password"]
        })
    if cur:
        if query["username"] == USER and query["password"] == PASSWD:
            print("came here")
            token = serializer.dumps({'username': USER})
            response = make_response(redirect(url_for("internal")))
            response.set_cookie("user", token, max_age=3600)
            return response
        return Response(status=200)
    return Response(status=400)

@app.route("/internal")
def internal():
    try:
        cookie = request.cookies.get("user")
        data = serializer.loads(cookie)
        username = data['username']
        if username == USER:
            return FLAG
    except SignatureExpired:
        return "Token expired"
    except BadSignature:
        return "Invalid token"
    except:
        return "Error"


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
