import json


class Songs:
    def __init__(self):
        try:
            with open("songs.json", "r") as f:
                self.songs = json.load(f)
        except FileNotFoundError:
            self.songs = []

    def all(self):
        return self.songs

    def get(self, id):
        song = [song for song in self.all() if song["id"] == id]
        if song:
            return song[0]
        return []

    def create(self, data):
        self.songs.append(data)

    def save_all(self):
        with open("songs.json", "w") as f:
            json.dump(self.songs, f)

    def update(self, id, data):
        song = self.get(id)
        if song:
            index = self.songs.index(song)
            self.songs[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        song = self.get(id)
        if song:
            self.songs.remove(song)
            self.save_all()
            return True
        return False


songs = Songs()