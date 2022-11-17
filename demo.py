import requests

from Branching import Plugin


@Plugin
def get_data(url):
    return requests.get(url)


@get_data.before
def hook(url: str):
    print("Requesting", url)


if __name__ == '__main__':
    print(get_data("https://www.baidu.com"))
