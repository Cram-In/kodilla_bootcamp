from flask import Flask, request, render_template, redirect
from app import app, db
from app.models import Author


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


@app.route("/author", methods=["POST"])
def add_author():
    content = request.form["content"]
    if not content:
        return "Error"

    author = Author(content)
    db.session.add(author)
    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return redirect("/")

    db.session.delete(task)
    db.session.commit()
    return redirect("/")


@app.route("/done/<int:task_id>")
def resolve_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return redirect("/")
    if task.done:
        task.done = False
    else:
        task.done = True

    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)