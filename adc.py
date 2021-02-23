from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')

bs = BeautifulSoup(url.read(), 'lxml')
title = bs.find_all(id='title', class_='text')
print(title)