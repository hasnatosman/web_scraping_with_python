from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(url, 'lxml')
# print(bs.h1.get_text())

for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)
