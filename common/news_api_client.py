import requests
from json import loads


NEWS_API_ENDPOINT = 'https://newsapi.org/v1/'
NEWS_API_KEY = 'b091a5dab00847dfb94daa52cfcb9fbe'

ARTICLE_API = 'articles'

BBC = 'bbc-news'
CNN = 'cnn'

SORT_BY_TOP = 'top'
SORT_BY_LATEST = 'latest'

DEFAULT_SOURCES = [CNN]


def build_url(endpoint = NEWS_API_ENDPOINT, api_name = ARTICLE_API):
    return endpoint + api_name


def get_news_by_sources(sources = DEFAULT_SOURCES, sortBy = SORT_BY_TOP):
    articles = []
    for source in sources:
        payload = {
            'source': source,
            'sortBy': sortBy,
            'apiKey': NEWS_API_KEY
        }
        response = requests.get(build_url(), params=payload)
        response_json = loads(response.content)

        if (response_json is not None
            and response_json['status'] == 'ok'
            and response_json['source'] is not None):

            for news in response_json['articles']:
                news['source'] = response_json['source']

            articles.extend(response_json['articles'])

    return articles
