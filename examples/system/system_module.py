import requests

from Branching import Plugin
from requests.models import Response


@Plugin
def get_data(url):
    return requests.get(url)


@get_data.before
def hook(url: str):
    print("Requesting", url)


@get_data.after(order=10)
def textify(url, _result: Response):
    print(type(_result), url)
    return _result.text
