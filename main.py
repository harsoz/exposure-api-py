from flask import Flask
from flask_cors import CORS
from controllers.home_controller import home
from controllers.bfs_controller import bfs
from controllers.dfs_controller import dfs
from controllers.star_controller import star

app = Flask(__name__)

CORS(app, resources={r"/api/v1/*": {"origins": "*"}}) 

app.register_blueprint(home, url_prefix='/api/v1/home')
app.register_blueprint(bfs, url_prefix='/api/v1/bfs')
app.register_blueprint(dfs, url_prefix='/api/v1/dfs')
app.register_blueprint(star, url_prefix='/api/v1/a_star')

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run()