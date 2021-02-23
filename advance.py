from urllib.request import urlopen
from bs4 import BeautifulSoup


url = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(url.read(), 'html.parser')

nameList = bs.find_all('span', {'class': {'green', 'red'}})

for name in nameList:
    print(name.get_text())