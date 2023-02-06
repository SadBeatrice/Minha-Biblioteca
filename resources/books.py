from flask_restful import Resource, reqparse
from models.book import BookModel

class Books(Resource):
    def get(self):
        return {'books': [book.json() for book in BookModel.query.all()]}, 200

class Book(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('título', type=str, required=True, help="The field 'título' cannot be left blank")
    arguments.add_argument('autor', type=str, required=True, help="The field 'autor' cannot be left blank")

    def get(self, id):
        book = BookModel.find_book(id)
        if book:
            return book.json(), 200
        return {'message': 'book not found.'}, 404  #not found

    def post(self, id):
        if BookModel.find_book(id):
            return {"message": "Book id '{}' already exists".format(id)}, 400

        data = Book.arguments.parse_args()
        book = BookModel(id, **data)
        try:
            book.save_book()
        except:
            return {'message': 'An internal error ocurred.'}, 500
        return book.json(), 200
        

    def put(self, id):
        data = Book.arguments.parse_args()        
        
        found_book = BookModel.find_book(id)
        if found_book:
            found_book.update_hotel(**data)
            try:
                found_book.save_book()
            except:
                return {'message': 'An internal error ocurred.'}, 500
            return found_book.json(), 200
        book = BookModel(id, **data)
        try:
            book.save_book()
        except:
            return {'message': 'An internal error ocurred.'}, 500
        return book.json(), 200

    def delete(self, id):
        book = BookModel.find_book(id)
        if book:
            book.delete_book()
            return {'message': 'Book deleted.'}
        return {'message': 'Book not found.'}, 404
