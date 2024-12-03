#!/usr/bin/env python3


import requests

url = "http://127.0.0.1:8000/suggestions/"


def get_suggestions_genres(genres):
    # test /productos post
    r = requests.post(url + "genre", json=genres)
    return r


genres = {"genres": ["Crime"]}
response_post = get_suggestions_genres(genres)
print(response_post.json())
