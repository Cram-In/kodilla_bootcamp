import requests
import random
import json

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NzM4OWQwZjdlNmI5NjJkYTgyZWRhM2FkMjcwOTg4MCIsInN1YiI6IjVmZWIwYTNlZDQwZDRjMDAzZTg1MjYwZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0kD6RaCKMHdn9ydafXlSLgypfmCHiVUqKcrV85oLOcU"


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_popular_movies():
    return call_tmdb_api(f"movie/polular")


def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    print(json.dumps(response.json(), indent=4))
    print(response.json()["cast"])
    return response.json()["cast"]


def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")


def get_lists():
    return call_tmdb_api(f"list/{list_id}")
