import os
import random
import requests
import sys

from lxml import html

CNN_CONTENT_XPATH = '''//div[contains(@class, 'zn-body__paragraph')]//text() | //p[contains(@class, 'zn-body__paragraph')]//text()'''

USER_AGENTS_FILE = os.path.join(os.path.dirname(__file__), 'user_agents.txt')
USER_AGENTS = []

with open(USER_AGENTS_FILE, 'rb') as uaf:
    for ua in uaf.readlines():
        if ua:
            USER_AGENTS.append(ua.strip()[1: -1])
random.shuffle(USER_AGENTS)


def get_headers():
    ua = random.choice(USER_AGENTS)
    headers = {
        'User-Agent': ua
    }
    return headers


def get_news_from_url(news_url):
    session = requests.session()
    response = session.get(news_url, headers=get_headers())

    try:
        tree = html.fromstring(response.content)
        news = tree.xpath(CNN_CONTENT_XPATH)
        news = ''.join(news)
    except Exception:
        return {}

    return news
