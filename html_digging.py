from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(url, 'lxml')

nameList = bsObj.findAll('span', {'class': 'green'})

for name in nameList:
    print(name.get_text())