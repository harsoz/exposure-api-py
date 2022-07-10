from flask import Blueprint, jsonify
from flask_cors import CORS
from services.home_service import is_cat

home = Blueprint('home', __name__)
CORS(home, resources={r"/api/v1/*": {"origins": "*"}})

@home.route('/cat/isCat', methods=['GET'])
def isCat():
    data_set = {"key1": [1, 2, 3], "key2": [4, 5, is_cat()]}
    return jsonify(data_set)