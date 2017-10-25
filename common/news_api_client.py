import requests
from json import loads


NEWS_API_ENDPOINT = ''
NEWS_API_KEY = ''

ARTICLE_API = 'articles'

BBC = 'bbc-news'
CNN = 'cnn'

SORT_BY_TOP = 'top'
SORT_BY_LATEST = 'latest'

DEFAULT_SOURCES = [CNN]

def getNewsBySources(sources = DEFAULT_SOURCES, sortBy = SORT_BY_TOP):
    articles = []
    for source in sources:
        url = NEWS_API_ENDPOINT + ARTICLE_API + '?source=' + source + '&sortBy=' + sortBy + '&apiKey=' + NEWS_API_KEY
