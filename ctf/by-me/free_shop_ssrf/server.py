from flask import Flask, Response, render_template, request
import requests

app = Flask(__name__)
with open("flag.txt", "r") as flag:
    FLAG = flag.read()

@app.route("/")
def home():
    return render_template("index.html")

def fetch_it(url):
    res = requests.get("http://localhost:8080/"+url)
    return res.text

@app.route("/buy", methods=("GET", "POST"))
def buy():
    try:
        pid = "getprice/"+request.form["product_id"]
        sid = "sale/"+request.form["coupon_code"]
        print(pid,sid)
        res = int(fetch_it(pid)) - int(fetch_it(sid))
        if not res:
            return FLAG
        return str(res) if res > 0 else f"{res} is negative, you can't buy."
    except:
        return "incorrect coupon_code or some error has occured."

@app.route("/proxy", methods=("POST", ))
def proxy():
    url = request.get_json()["t"]
    return fetch_it(url)