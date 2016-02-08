#from app import app
#app.debug = True
#app.run(host='0.0.0.0', port=5005)
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
