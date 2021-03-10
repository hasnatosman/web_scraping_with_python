from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('https://evaly.com.bd/shops')

bs = BeautifulSoup(url, 'lxml')
print(bs)