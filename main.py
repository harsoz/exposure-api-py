from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.home_controller import home
from controllers.bfs_controller import bfs
from shared.helpers import is_legal_pos, offsets
from shared.queue_al import Queue

app = Flask(__name__)

CORS(app, resources={r"/api/v1/*": {"origins": "*"}}) 

app.register_blueprint(home, url_prefix='/api/v1/home')
# app.register_blueprint(bfs, url_prefix='/api/v1/bfs')

@app.route('/')
def index():
    return "Hello World!"

@app.route('/api/v1/bfs/compute', methods=['POST'])
def compute():
    body = request.json  
    queue = Queue()
    queue.enqueue(tuple(body['start']))
    predecessors = { "start": None}
    path = []

    while not queue.is_empty():
        current_cell = queue.dequeue()
        x, y = current_cell

        # send tuple as list for react
        path.append([x, y])

        if current_cell == tuple(body['goal']):
            return jsonify(path)

        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neigbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(body['maze'], neigbour) and neigbour not in predecessors:
                queue.enqueue(neigbour)
                predecessors[neigbour] = current_cell
    return None

if __name__ == "__main__":
    app.run()