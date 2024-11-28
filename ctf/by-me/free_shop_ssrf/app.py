from api import api
from server import app
import threading

if __name__ == '__main__':
    API = threading.Thread(target=api.run, args=("localhost",8080))
    SERVER = threading.Thread(target=app.run, args=("0.0.0.0",5000))
    API.start()
    SERVER.start()