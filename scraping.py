import requests
from bs4 import BeautifulSoup

DESIRED_HUBS = {'Научно-популярное' ,'C#'}

response = requests.get('https://habr.com/ru/all/')
if not response.ok:
    raise ValueError('no response')

text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')
print(len(articles))

for article in articles:
    hubs = {h.text for h in article.find_all('a',class_='tm-article-snippet__hubs-item-link')}
    if DESIRED_HUBS & hubs:
        href = article.find('a', class_='tm-article-snippet__title_link').attrs.get('href')
        print(href)