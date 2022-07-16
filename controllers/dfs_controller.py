from flask import Blueprint, jsonify, request
from shared.helpers import get_path, is_legal_pos, offsets
from shared.stack import Stack

dfs = Blueprint('dfs', __name__)

@dfs.route('/compute', methods=['POST'])
def compute():
    body = request.json
    stack = Stack()
    stack.push(tuple(body['start']))
    predecessors = {"start": None}

    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == tuple(body['goal']):
            return jsonify(get_path(predecessors, tuple(body['start']), tuple(body['goal']) ))

        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset,
                        current_cell[1] + col_offset)
            if is_legal_pos(body['maze'], neighbor) and neighbor not in predecessors:
                stack.push(neighbor)
                predecessors[neighbor] = current_cell

    return None
