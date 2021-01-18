from flask import Flask, request, render_template, redirect, url_for
from forms import TodoForm
import sqlite3
from models import Todos

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/")
def todo_list():
    form = TodoForm()
    error = ""
    conn = sqlite3.connect("todos.db")
    c = conn.cursor()
    c.execute("SELECT * FROM todo")
    todos = c.fetchall()
    return render_template("todos.html", form=form, error=error, todos=todos)


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    form = TodoForm()
    error = ""
    conn = sqlite3.connect("todos.db")
    c = conn.cursor()
    c.execute("SELECT todo.id FROM todo")
    todo = c.fetchall()
    c.execute(
        "DELETE from todo WHERE id = :id",
        {"id": task_id},
    )
    conn.commit()
    return redirect("/")


@app.route("/new/", methods=["POST"])
def new_item():
    form = TodoForm()
    error = ""
    title = request.form["title"]
    descryption = request.form["description"]
    conn = sqlite3.connect("todos.db")
    c = conn.cursor()
    c.execute("INSERT INTO todo (title, description) VALUES (?,?)", (title, descryption))
    new_id = c.lastrowid
    conn.commit()
    c.close()

    return redirect("/")


@app.route("/update/<int:task_id>", methods=["GET"])
def update_task(task_id):
    form = TodoForm()
    error = ""
    conn = sqlite3.connect("todos.db")
    c = conn.cursor()
    c.execute("SELECT todo.id FROM todo")
    todo = c.fetchall()
    print(todo)
    print(task_id)
    return render_template("/todo_id/", form=form, error=error)
    # if request.GET.get("save", "").strip():
    #    edit = request.GET.get("title", "").strip()
    #
    #    conn = sqlite3.connect("todos.db")
    #    c = conn.cursor()
    #    c.execute("UPDATE todo SET title = ?, description = ? WHERE id LIKE ?", (edit, no))
    #    conn.commit()
    #
    #    return render_template("todos_id.html", form=form, error=error)
    # else:
    #    conn = sqlite3.connect("todos.db")
    #    c = conn.cursor()
    #    c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
    #    cur_data = c.fetchone()
    #
    #    return render_template("todos.html", form=form, error=error, todos=todos)


if __name__ == "__main__":
    app.run(debug=True)