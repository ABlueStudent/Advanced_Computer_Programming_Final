import requests
from bs4 import BeautifulSoup

class playUSpider():
    def __init__(self):
        self.url = 'https://news.ubisoft.com/en-us/'
        
    def makeSoup(self):
        cache = requests.get(self.url)
        soup = BeautifulSoup(cache.text, 'html.parser')

        return soup
    
    def contentList(self):
        soup = self.makeSoup()
        content = map(lambda item: {
            'title': item.find('h2', 'updatesPagination__item__wrapper__content__title').text,
            'description': item.find('p', 'updatesPagination__item__wrapper__content__abstract').text,
            'date': item.find('span', 'date').text,
            'readtime': item.find('span', 'updatesPagination__item__wrapper__content__min').text
        },
        soup.findAll('a', 'updatesPagination__item'))
        content = list(content)

        return content