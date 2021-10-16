from types import MethodType
from flask import Blueprint

# is hello_world our endpoint?
hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route('/hello-world', methods=["GET"])
def get_hello_world():
    my_response = "Hello, World!"
    return my_response

@hello_world_bp.route('/hello-world/JSON', methods=['GET'])
def hello_world_json():
    return {
        "name": "Mariah",
        "message": "Ciao!",
        "hobbies": "coding"
    }, 200