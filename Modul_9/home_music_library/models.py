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
        return self.songs[id]

    def create(self, data):
        #data.pop('csrf_token')
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