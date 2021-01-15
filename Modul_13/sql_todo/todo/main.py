from flask import Flask, render_template, request, redirect, url_for, flash
from config import app
from models import add_task
from forms import TodoForm


@app.route("/", methods=["GET", "POST"])
@app.route("/todo.html/", methods=["GET", "POST"])
def songs_list():
    form = TodoForm()
    error = ""
    if request.method == "POST":
        task = {"task": request.form["title"], "task": request.form["description"]}

        try:
            c = conn.cursor()
            add_task(task)
            conn.close()
            return redirect("/")
        except:
            return "There was an issue adding your task"

    else:

        return render_template("todo.html")


@app.route("/delete/<int:task_id>", methods=["GET"])
def delete_task(task_id):
    pass


@app.route("/update/<int:task_id>/", methods=["GET", "POST"])
def update_task(song_id):
    pass


if __name__ == "__main__":
    app.run(debug=True)