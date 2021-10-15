import json


class CountryIterator:
    def __init__(self, country_list):
        """
        country_list список словарей со странами
        """
        self.country_list = country_list
        self.cursor = 0

    def __iter__(self):
        return self

    def make_link(self, country):
        """
        Здесь логика получения ссылки0
        """
        link = f'https://en.wikipedia.org/wiki/{country}'
        return link

    def __next__(self):
        """
        здесь логика имзенения self.cursor и StopIteration
        """
        self.cursor += 1

        country = self.country_list[self.cursor]['name']['common']
        link = self.make_link(country)
        if self.cursor == len(self.country_list) - 1:
            raise StopIteration
        return link



with open('countries.json', 'r', encoding='utf-8') as c:

    country_list = json.load(c)




with open('country_links.txt', 'w', encoding='utf-8') as country_links_file:
    for country_link in CountryIterator(country_list):
        country_links_file.write(f'{country_link}\n')
