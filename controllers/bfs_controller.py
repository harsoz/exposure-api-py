from flask import Blueprint, jsonify, request
from shared.helpers import get_path, is_legal_pos, offsets
from shared.queue_al import Queue

bfs = Blueprint('bfs', __name__)

@bfs.route('/compute', methods=['POST'])
def compute():
    body = request.json  
    queue = Queue()
    queue.enqueue(tuple(body['start']))
    predecessors = { "start": None}

    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == tuple(body['goal']):
            return jsonify(get_path(predecessors, tuple(body['start']), tuple(body['goal']) ))

        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neigbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(body['maze'], neigbour) and neigbour not in predecessors:
                queue.enqueue(neigbour)
                predecessors[neigbour] = current_cell
    return None