from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


try:
    html = urlopen('https://www.python.org/')
except HTTPError as e:
    print(e)
except URLError as e:
    print("Server couldn't found")
else:
    print('It is working.')