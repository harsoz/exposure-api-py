from flask import Flask

app = Flask(__name__)


@app.route("/diana/prueba")
def hello():
    return "Hello, World!"


@app.route("/diana/prueba2")
def hello1():
    
    return "Hello, putos!"

app.run()
