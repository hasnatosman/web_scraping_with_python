import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.goal.com/en-in')  # using the requests module , we use the get function
# print(result.status_code)

# we store page content to a variable 'src'
src = result.content
# print(src)

#  we stored the page, now we will use the Beautiful module to parse the source
# create a BeautifulSoup object name 'soup'

soup = BeautifulSoup(src, 'lxml')

# here i will find all the a tag , and store it on links variable

links = soup.find_all('a')
# print(links)
# print('\n')


# now we will find all the text that contains 'About' on the page instead of every link
for link in links:
    if 'Klopp' in link.text:
        print(link)
        print(link.attrs['href'])

# print(result.status_code)
# using status code we see that url is ok


# print(result.headers)
