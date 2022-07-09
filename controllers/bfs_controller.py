from flask import Blueprint, jsonify, request
from shared.helpers import is_legal_pos, offsets
from shared.queue_al import Queue

bfs = Blueprint('bfs', __name__)

@bfs.route('/bfs/compute', methods=['POST'])
def compute():
    content_type = request.headers.get('Content-Type')
    body = ""
    if (content_type == 'application/json'):
        body = request.json   
     
    queue = Queue()
    test = tuple(body['start'])
    queue.enqueue(tuple(body['start']))
    predecessors = { "start": None}

    while not queue.is_empty():
        current_cell = queue.dequeue()

        if current_cell == tuple(body['goal']):
            return "yeah"

        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neigbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(body['maze'], neigbour) and neigbour not in predecessors:
                queue.enqueue(neigbour)
                predecessors[neigbour] = current_cell
    return None