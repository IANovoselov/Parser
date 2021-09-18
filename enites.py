from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


class Filtr():
    def __init__(self, link):
        self.link = link
        self.out_put = []
        self.article = {'date': '', 'author': '', 'title': '', 'text': ''}
        self.response = requests.get(self.link, headers={'User-Agent': UserAgent().chrome})
        self.response.encoding = 'utf-8'
        self.soup = BeautifulSoup(self.response.text, 'lxml')

    def content_p(self, div):
        """информаия, содержащаяся в параграфах"""
        for p in div.find_all('p'):
            self.out_put.append(p.text)
        return self.out_put

    def finder(self):
        """главный метод, осуществляет поиск таких эдементов разметки div"""
        answer = []
        answer.extend(self.content_p(self.soup.find('div', {"class": "b-topic__content"})))

        self.article['date'] = self.soup.find('time')['datetime'].strip()
        self.article['title'] = self.soup.title.text
        self.article['author'] = answer[-1]
        self.article['text'] = ''.join(answer[:-1])

        return self.article
