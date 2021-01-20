from app import db


bookshelf = db.Table(
    "bookshelf",
    db.Model.metadata,
    db.Column("author_id", db.Integer, db.ForeignKey("authors.author_id")),
    db.Column("book_id", db.Integer, db.ForeignKey("books.book_id")),
)


class Author(db.Model):
    __tablename__ = "authors"
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, nullable=True)
    surname = db.Column(db.String(20), index=True, nullable=True)
    birth = db.Column(db.String(15), index=True, nullable=True)
    books = db.relationship("Book", secondary=bookshelf, lazy="dynamic")

    def __repr__(self):
        return f"<Author: {self.name} {self.surname}>"


class Book(db.Model):
    __tablename__ = "books"
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), index=True, nullable=True)
    genre = db.Column(db.String(15), index=True, nullable=True)
    pages = db.Column(db.Integer, index=True, nullable=True)
    stock = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Book: '{self.title}'. On shelf: {self.stock}>"


# a = Author()
# b = Book()
# a.book.append(b)
# db.session.add(a)
# db.session.commit()
