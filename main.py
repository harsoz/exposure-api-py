from flask import Flask
from controllers.home_controller import home

app = Flask(__name__)

app.register_blueprint(home, url_prefix='/api')

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run()