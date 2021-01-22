import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NzM4OWQwZjdlNmI5NjJkYTgyZWRhM2FkMjcwOTg4MCIsInN1YiI6IjVmZWIwYTNlZDQwZDRjMDAzZTg1MjYwZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0kD6RaCKMHdn9ydafXlSLgypfmCHiVUqKcrV85oLOcU"


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_lists():
    endpoint = "https://api.themoviedb.org/3/list/{list_id}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    return response.json()


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()
