import requests
from enum import Enum, unique


class News:
    url_src = 'https://newsapi.org/v1/sources?language=en'
    url_art = 'https://newsapi.org/v1/articles?'
    key = '&apiKey=70f3c8a6803245d8b911af04f6eff00c'
    # r = requests.get(url_src+key)
    # src = r.json()['sources']
    # r = requests.get(url_art+key)
    # art = r.json()['articles']

    def __init__(self, key='70f3c8a6803245d8b911af04f6eff00c'):
        self.key2 = key

    def fetchall_arts(self, src):
        src_art = 'source='+src
        r = requests.get(self.url_art+src_art+self.key)
        art = r.json()['articles']
        return art

    def news_sources(self):
        src = {'src' : 'bloomberg'}
        return src

@unique
class NEWS_SRC(Enum):
    ABC = 'success'
    BLOOMBERG = 'bloomberg'
