import json
from urllib.request import urlopen


class Weather:
    __resultado=None
    def __init__(self):
        self.__resultado=None
    def run(self, url):
        url_template = url
        response = urlopen(url_template)
        self.__resultado = json.loads(response.read().decode())
    def getResultado(self):
        return self.__resultado