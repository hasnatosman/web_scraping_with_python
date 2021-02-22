from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(page.read(), 'lxml')

print(bs.h1)