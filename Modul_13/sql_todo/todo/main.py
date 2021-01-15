from flask import Flask, render_template, request, redirect, url_for, flash
from config import app
from models import Todos, get_all
import sqlite3
import uuid


@app.route("/", methods=["GET", "POST"])
@app.route("/todo.html/", methods=["GET", "POST"])
def all_tasks():
    if request.method == "POST":
        with sqlite3.connect("todo.db") as conn:
            task_id = uuid.uuid4()
            task_id = str(task_id)
            title = request.form["title"]
            description = request.form["description"]
            c = conn.cursor()
            c.execute("INSERT INTO todo VALUES (?, ?, ?)", (task_id, title, description))
            conn.commit()

            return redirect("/")
    else:
        with sqlite3.connect("todo.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM todo")
            tasks = c.fetchall()
            return render_template("todo.html", tasks=tasks)


@app.route("/delete/{{task[0]}}")
def delete_task(task_id):
    task_id = task[0]
    print("==================>", task_id)
    with sqlite3.connect("todo.db") as conn:
        c = conn.cursor()
        c.execute("DELETE from todo WHERE (?)", (task_id))
        tasks = c.fetchall()
        return redirect("/")


@app.route("/update/<int:task_id>/", methods=["GET", "POST"])
def update_task(task_id):
    pass


if __name__ == "__main__":
    app.run(debug=True)