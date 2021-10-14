import requests
from bs4 import BeautifulSoup

DESIRED_HUBS = {'Научно-популярное ', 'C# *', 'Big Data '}

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise ValueError('no response')

text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    hubs = {h.text for h in article.find_all('a', class_='tm-article-snippet__hubs-item-link')}
    time = {t.text for t in article.find('time')}
    headline = {head.text for head in article.find('a', class_='tm-article-snippet__title-link')}

    if DESIRED_HUBS & hubs:
        href = article.find('a', class_='tm-article-snippet__hubs-item-link').attrs.get('href')
        print(headline)
        print(time)
        print(f'https://habr.com/ru{href}')
