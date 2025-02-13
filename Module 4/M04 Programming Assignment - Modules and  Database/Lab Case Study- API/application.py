from urllib import request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating the Flask app
app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.book_name} by {self.author} published by {self.publisher}'

    
@app.route('/')
def index():
    return 'Hello!'

# get all books 
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = [] 

    for book in books:
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {"books": output}

# Get a single book
@app.route('/books/<id>')
def get_single_book(id):
    book = Book.query.get_or_404(id)
    return {"book_name": book.book_name, "author": book.author, "publisher": book.publisher}


# post and add a book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(new_book)
    db.session.commit()
    return {"id": new_book.id}

# update a book
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    book.book_name = request.json['book_name']
    book.author = request.json['author']
    book.publisher = request.json['publisher']
    db.session.commit()
    return {"message": "Book updated successfully"}

# delete a book
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return {"message": "Book deleted successfully"}