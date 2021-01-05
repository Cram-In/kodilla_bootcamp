from flask import Flask, jsonify, abort, make_response, request
from models import songs


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/api/v1/songs/", methods=["GET"])
def songs_list_api():
    return jsonify(songs.all())


@app.route("/api/v1/songs/<int:song_id>/", methods=["GET"])
def get_song(song_id):
    print("=====>", song_id)
    song = songs.get(song_id)
    if not song:
        abort(404)
    return jsonify({"song": song})


@app.route("/api/v1/songs/", methods=["POST"])
def add_song():
    if not request.json or not "title" in request.json:
        abort(400)
    print(request.json)
    song = {
        "id": songs.all()[-1]["id"] + 1,
        "title": request.json.get("title"),
        "band": request.json.get("band", ""),
        "genre": request.json.get("genre", ""),
    }
    songs.create(song)
    return jsonify({"song": song}), 201


@app.route("/api/v1/songs/<int:song_id>/", methods=["DELETE"])
def delete_song(song_id):
    result = songs.delete(song_id)
    if not result:
        abort(404)
    return jsonify({"result": result})


@app.route("/api/v1/songs/<int:song_id>/", methods=["PUT"])
def update_song(song_id):
    song = songs.get(song_id)
    print(song)
    if not song:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any(
        [
            "title" in data and not isinstance(data.get("title"), str),
            "band" in data and not isinstance(data.get("band"), str),
            "genre" in data and not isinstance(data.get("genre"), str),
        ]
    ):
        abort(400)
    song = {
        "id": song_id,
        "title": data.get("title", song["title"]),
        "band": data.get("band", song["band"]),
        "genre": data.get("genre", song["genre"]),
    }
    songs.update(song_id, song)
    return jsonify({"song": song})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found", "status_code": 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request", "status_code": 400}), 400)


if __name__ == "__main__":
    app.run(debug=True)