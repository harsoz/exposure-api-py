from flask import Flask
from flask_cors import cross_origin
from controllers.home_controller import home
from controllers.bfs_controller import bfs

app = Flask(__name__)
app.register_blueprint(home, url_prefix='/api/v1/home')
app.register_blueprint(bfs, url_prefix='/api/v1/bfs')

@app.route('/')
@cross_origin()
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run()