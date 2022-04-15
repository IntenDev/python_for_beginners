from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
# html = urlopen('https://www.salon-love-forever.ru/wedding/kaplun/inda/')
# print(html.read())
# bs = BeautifulSoup(html, 'html.parser')
# print(bs.title)
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.title
    except AttributeError as e:
        return None
    return title
def getDescription(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        description = bs.find('meta', {'name':'description'})
    except AttributeError as e:
        return None
    return description

title = getTitle('https://www.salon-love-forever.ru/wedding/kaplun/inda/')
description = getDescription('https://www.salon-love-forever.ru/wedding/kaplun/inda/')
if title == None:
    print('Title could not be found')
else:
    print(title)
if description == None:
    print('Description could not be found')
else:
    print(description)