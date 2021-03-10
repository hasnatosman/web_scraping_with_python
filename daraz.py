from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('https://www.daraz.com.bd/')

bs = BeautifulSoup(url, 'lxml')
print(bs.h1)