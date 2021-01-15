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


@app.route("/delete/<int:song_id>", methods=["GET"])
def delete_task(task_id):
    form = MusicLibrary()
    error = ""
    song = songs.delete(song_id - 1)
    songs.save_all()
    if not song:
        abort(404)

    return render_template("index.html", form=form, songs=songs.all(), error=error)


@app.route("/update/<int:song_id>/", methods=["GET", "POST"])
def update_song(song_id):
    song = songs.get(song_id - 1)
    form = MusicLibrary(data=song)
    error = ""

    if request.method == "POST":
        if form.validate_on_submit():
            songs.update(song_id - 1, form.data)
            songs.save_all()
        return redirect(url_for("songs_list"))

    return render_template("index_id.html", form=form, song_id=song_id, error=error)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request", "status_code": 400}), 400)


if __name__ == "__main__":
    app.run(debug=True)