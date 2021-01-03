from flask import Flask, request, render_template, redirect, url_for, json
from forms import MusicLibrary
from models import songs


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/", methods=["GET", "POST"])
@app.route("/index.html/", methods=["GET", "POST"])
def songs_list():
    form = MusicLibrary()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            songs.create(form.data)
            songs.save_all()
        return redirect(url_for("songs_list"))
    
    return render_template("index.html", form=form, songs=songs.all(), error=error)

@app.route("/delete/<int:song_id>", methods=["GET"])
def delete_song(song_id):
    form = MusicLibrary()
    error = ""
    song = songs.delete(song_id-1)
    songs.save_all()
    if not song:
        abort(404)
    
    return render_template("index.html", form=form, songs=songs.all(), error=error)

@app.route("/update/<int:song_id>/", methods=["GET", "POST"])
def update_song(song_id):
    song = songs.get(song_id-1)
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
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)


if __name__ == "__main__":
    app.run(debug=True)