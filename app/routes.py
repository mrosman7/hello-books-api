from types import MethodType
from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.book import Book

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route('', methods=['POST', 'GET'])
def handle_books():
    if request.method == 'POST':
        request_body = request.get_json()

        if 'title' not in request_body or 'description' not in request_body:
            return make_response("Invalid Request", 400)

        new_book = Book(
            title = request_body['title'],
            description = request_body['description']
        )
        db.session.add(new_book)
        db.session.commit()

        return make_response(
            f'Book {new_book.title} created', 201
        )

    elif request.method == 'GET':
        title_from_url = request.args.get('title')
        if title_from_url:
            books = Book.query.filter_by(title=title_from_url)
        else:
            books = Book.query.all()

        books_response = []
        for book in books:
            books_response.append(book.to_dict())
        return jsonify(books_response)

@books_bp.route('/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(book_id):
    
    book = Book.query.get(book_id)

    if request.method == 'GET':
        if not book:
            return {
                "message": f"Book {book_id} does not exist"
            }, 404
        return jsonify(book.to_dict())
    elif request.method == 'PUT':
        request_body = request.get_json()
        if not 'title' in request_body or not 'description' in request_body:
            return {
                "message": "Request requires both a title and description"
            }, 400
        book.title = request_body['title']
        book.description = request_body['description']

        #Save Action
        db.session.commit()

        return jsonify(book.to_dict()), 200

    elif request.method == 'DELETE':
        if not book:
            return {
                "message": f"Book not found"
            }, 404

        db.session.delete(book)
        db.session.commit()

        return {
            "Message": f"Book with title {book.title} has been deleted"
        }, 200