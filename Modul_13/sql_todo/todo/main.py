from flask import Flask, render_template, request, redirect, url_for, flash
from config import app
from models import add_task


@app.route("/", methods=["GET", "POST"])
@app.route("/todo.html/", methods=["GET", "POST"])
def songs_list():
    if request.method == "POST":
        task = {"task": request.form["title"], "task": request.form["description"]}

        try:
            c = conn.cursor()
            add_task(task)
            conn.close()
            return redirect("/")
        except Exception as e:
            print(e)

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