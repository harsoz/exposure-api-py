from shared.priority_queue import PriorityQueue
from flask import Blueprint, jsonify, request
from shared.helpers import is_legal_pos, offsets

star = Blueprint('star', __name__)


@star.route('/compute', methods=['POST'])
def compute():
    body = request.json
    pq = PriorityQueue()
    pq.put(tuple(body['start']), 0)
    predecessors = {"start": None}
    g_values = {"start": 0}
    path = []
    while not pq.is_empty():
        current_cell = pq.get()
        x, y = current_cell
        path.append([x, y])
        if current_cell == tuple(body['goal']):
            return jsonify(path)

        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neigbour = (current_cell[0] + row_offset,
                        current_cell[1] + col_offset)

            if is_legal_pos(body['maze'], neigbour) and neigbour not in g_values:
                current_cell_value = 0 if current_cell not in g_values else g_values[current_cell]
                new_cost = current_cell_value + 1
                g_values[neigbour] = new_cost
                f_value = new_cost + heuristic(tuple(body['goal']), neigbour)
                pq.put(neigbour, f_value)
                predecessors[neigbour] = current_cell

    return None


def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)
