# import sqlite3
#
# # create a connection to the database
# # if the database doesn't exist then it will be created
#
# db = sqlite3.connect("books-collection.db")
#
# # create a cursor which will control our database
#
# cursor = db.cursor()
#
# # create a table
# # execute() method tells the cursor to execute an action
#
# # cursor.execute("create table books(id integer primary key, title varchar(250) not null unique, author varchar(250) not null, rating float not null)")
#
# # add data to table
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
#
# # there are much better ways of working with SQLite in Python projects,
# # we can use a tool called SQLAlchemy to write Python code instead of all these error-prone SQL commands.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create table

with app.app_context():
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.Float, nullable=False)

        # print each book object  with its title
        def __repr__(self):
            return f"<Book {self.title}>"

    db.create_all()

    # create  new record
    # new_book = Book(title="Harry", author="Ramesh", rating=8.5)
    # db.session.add(new_book)
    # db.session.commit()

    # read all records
    all_books = db.session.query(Book).all()
    print(all_books)

    # read a particular record by query
    # book = Book.query.filter_by(title="Harry").first()
    # print(book)

    # update a particular record by query
    # book_to_update = Book.query.filter_by(title="Harry Potter").first()
    # book_to_update.title = "Harry Potter and a Dog"
    # db.session.commit()

    # update a record by primary key
    # book_id = 1
    # book_to_update = Book.query.get(book_id)
    # book_to_update.title = "Harry Potter and Cathy"
    # db.session.commit()

    # delete a particular record by primary key
    book_id = 1
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    # Note: can also delete data by querying for a particular value e.g. by title or one of the other properties
