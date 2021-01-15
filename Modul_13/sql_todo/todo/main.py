from flask import Flask, render_template, request, redirect, url_for, flash
from config import app
from models import add_task, Todos
import sqlite3


@app.route("/", methods=["GET", "POST"])
@app.route("/todo.html/", methods=["GET", "POST"])
def songs_list():
    if request.method == "POST":
        with sqlite3.connect("todo.db") as conn:
            id = 1
            title = request.form["title"]
            description = request.form["description"]
            c = conn.cursor()
            c.execute("INSERT INTO todo VALUES (?, ?, ?)", (id, title, description))
            conn.commit()
            return redirect("/")
    else:
        return render_template("todo.html")


@app.route("/delete/<int:id>")
def delete_task(id):
    pass


@app.route("/update/<int:id>/", methods=["GET", "POST"])
def update_task(id):
    pass


if __name__ == "__main__":
    app.run(debug=True)