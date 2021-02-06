from urllib.request import urlopen

url = urlopen('https://pythonscraping.com/pages/page1.html')

print(url.read())