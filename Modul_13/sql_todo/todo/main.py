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


@app.route("/delete/<string:task_id>", methods=["GET"])
def delete_task(task_id):
    with sqlite3.connect("todo.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM todo")
        tasks = c.fetchall()
        c.execute(
            "DELETE from todo WHERE task_id = :task_id",
            {"task_id": task_id},
        )
        conn.commit()
        return redirect("/")


@app.route("/update/<string:task_id>/", methods=["GET", "POST"])
def update_task(task_id):
    with sqlite3.connect("todo.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM todo")
        tasks = c.fetchall()
        print(task_id)
        return render_template("todo_id.html")
        title = request.form["title"]
        description = request.form["description"]
        print(title)
        print(description)
        print(task_id)
        c.execute(
            """UPDATE todo SET title = title, description = description
                    WHERE task_id = taks_id""",
            {"title": title, "description": description},
        )
        conn.commit()
    return render_template("todo.html", task_id=task_id)


if __name__ == "__main__":
    app.run(debug=True)