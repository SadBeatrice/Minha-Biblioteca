from flask import Flask
from flask_restful import Api
from resources.books import Books, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_database():
    database.create_all()

api.add_resource(Books, '/books')
api.add_resource(Book, '/books/<string:id>')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True)

# http://127.0.0.1:5000/books