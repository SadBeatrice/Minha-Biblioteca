from sql_alchemy import database

class BookModel(database.Model):
    __tablename__ = 'books'

    id = database.Column(database.String, primary_key=True)
    título = database.Column(database.String(80))
    autor = database.Column(database.String(60))

    def __init__(self, id, título, autor):
        self.id = id
        self.título = título
        self.autor = autor

    def json(self):
        return {
            'id': self.id,
            'título': self.título,
            'autor': self.autor
        }

    @classmethod
    def find_book(cls, id):
        book = cls.query.filter_by(id=id).first()   # select * from books where id = idpassado
        if book:
            return book
        return None

    def save_book(self):
        database.session.add(self)
        database.session.commit()

    def update_hotel(self, título, autor):
        self.título = título
        self.autor = autor

    def delete_book(self):
        database.session.delete(self)
        database.session.commit()