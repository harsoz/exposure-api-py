from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from shared.helpers import is_legal_pos, offsets
from shared.queue_al import Queue

bfs = Blueprint('bfs', __name__)

@bfs.route('/compute', methods=['POST'])
@cross_origin()
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