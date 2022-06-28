import json
from urllib.request import urlopen


class DOLARSI:
    __resultado=None
    def __init__(self):
        self.__resultado=None
    def run(self):
        url_template = 'https://www.dolarsi.com/api/api.php?type=dolar'
        response = urlopen(url_template)
        self.__resultado = json.loads(response.read().decode())
    def getResultado(self):
        return self.__resultado