import requests
from config import Config


def list_movies_by_search(query, page=1):

    url = f"{Config.OMDB_API_BASE}?apikey={Config.OMDB_API_KEY}&s={query}&page={page}"
    req = requests.get(url)
    res = req.json()
    if res["Response"] == "True":
        return res["Search"]
    return []


def get_movie_detail(imdb_id):
    url = f"{Config.OMDB_API_BASE}?apikey={Config.OMDB_API_KEY}&i={imdb_id}&plot=full"
    req = requests.get(url)
    return req.json()
