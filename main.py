from flask import Flask
from controllers.home_controller import home
from controllers.bfs_controller import bfs

app = Flask(__name__)

app.register_blueprint(home, url_prefix='/api')
app.register_blueprint(bfs, url_prefix='/api')

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run()