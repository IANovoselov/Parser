from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

link = input('Enter link: ')


class Filtr():
    def __init__(self, link):
        self.link = link
        self.out_put = []
        self.author = ''
        self.title = ''
        self.date = ''
        self.response = requests.get(self.link, headers={'User-Agent': UserAgent().chrome})
        self.response.encoding = 'utf-8'
        self.soup = BeautifulSoup(self.response.text, 'lxml')

    def fname(self):
        '''формируется имя файла'''
        return 'name.txt'

    def content_p(self, div):
        '''если в div более 2 p, то метод вытаскивыет текстовую информацию, предварительно вставив ссылки'''
        if 2 < len(div.find_all('p')) < 9:
            for p in div.find_all('p'):
                p = p.text
                self.out_put.append(p)
        return self.out_put


    def part_of_strings(self, string):
        '''возвращает строку длиной не более 80 символов'''
        if len(string) > 80:
            if string[80] == ' ':
                return string[0:80]
            else:
                for i in range(79, 0, -1):
                    if string[i] == ' ':
                        return string[0:i]
        else:
            return string

    def writer(self, string, file_name):
        '''принимает строку, делит на подстроки с помощью метода part_of_strings() и записывает в файл, отбивая абзац пустой строкой'''
        while string != '':
            ans = (self.part_of_strings(string))
            print(ans, file=file_name, end='\n')
            if len(ans) == len(string):
                string = ''
            else:
                string = string[len(ans):].lstrip()

    def finder(self):
        '''главный метод, осуществляет поиск таких эдементов разметки html, как article, div , p'''
        answer = []
        for div in self.soup.find_all('div'):
            answer.extend(self.content_p(div))

        new_out = []
        for x in answer:
            # исключаем оставшися мусор по типу "\t\n\n\n\Подпишись!"
            if x not in new_out and ('\n' or '\r' or '\t' ) not in x:
                if x != '':
                    new_out.append(x)

        self.date = self.soup.find('time')['datetime'].strip()
        self.title = self.soup.title.text
        self.author = new_out[-1]
        self.out_put = new_out[:-1]

        print(self.date)
        print(self.title)
        print(self.author)
        print(self.out_put)

        with open(self.fname(), 'w') as fl: #открываем файл, записываем информацию
            self.writer(self.soup.title.text, fl)
            print('\n', file=fl, end='')
            for x in new_out:
                self.writer(x, fl)
                print('\n', file=fl, end='')


one = Filtr(link)
one.finder()
