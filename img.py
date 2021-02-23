from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('http://www.pythonscraping.com/pages/page3.html')

bs = BeautifulSoup(url.read(), 'lxml')
title = bs.find_all('h1')
print(title)