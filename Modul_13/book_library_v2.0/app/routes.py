from flask import Flask, request, render_template, redirect
from app import app, db
from app.models import Author, Book


@app.route("/")
def book_list():
    books = Book.query.all()
    return render_template("books.html", books=books)


@app.route("/book", methods=["POST"])
def add_book():
    content = request.form["content"]
    if not content:
        return "Error"

    book = Book(content)
    db.session.add(book)
    db.session.commit()
    return redirect("/")


@app.route("/author?", methods=["POST"])
def add_author():
    content = request.form["content"]
    if not content:
        return "Error"

    author = Author(content)
    db.session.add(author)
    db.session.commit()
    return redirect("/")


@app.route("/assign/")
def assign_book(author_id):  # assign book to author
    pass


@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    pass
    """
    book = Book.query.get(book_id)
    if not book:
        return redirect("/")

    db.session.delete(book)
    db.session.commit()
    return redirect("/")
    """


@app.route("/delete/<int:author_id>")
def delete_author(author_id):
    pass
    """
    author = Author.query.get(author_id)
    if not author:
        return redirect("/")

    db.session.delete(author)
    db.session.commit()
    return redirect("/")
    """


@app.route("/stock/<int:book_id>")
def books_stock_control(book_id):
    book = Book.query.get(book_id)

    if not book:
        return redirect("/")
    if Book.done:
        Book.done = False
    else:
        Book.done = True

    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)