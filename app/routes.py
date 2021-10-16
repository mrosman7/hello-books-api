from types import MethodType
from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Where the Crawdads Sing", "A good book about a swamp girl"),
    Book(2, "The Vanishing Half", "A story about two estranged sisters entwined lives"),
    Book(3, "Educated", "A memior about a young girl escaping religious cult.")
] 

# is hello_world our endpoint?
hello_world_bp = Blueprint("hello_world_bp", __name__)

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=['GET'])
def handle_books():
    books_response = []

    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)

@books_bp.route('/<book_id>', methods=['GET'])
def handle_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }



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

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    
    return response_body