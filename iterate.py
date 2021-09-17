import requests
import json

class Myrange:
    def __init__(self, start, end):
        self.start, self.end = start-1, end

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.start

countries_dict = {}

with open('countries.json', 'r', encoding='utf-8') as c:

    countries = json.load(c)
    for number in Myrange(0, len(countries) - 1):
        country = countries[number]['name']['common']
        countries_dict[country] = f'https://en.wikipedia.org/wiki/{country}'

    print(countries_dict)
json.dumps(list(countries_dict))