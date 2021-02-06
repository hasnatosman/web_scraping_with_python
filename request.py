import urllib.request

with urllib.request.urlopen('https://pythonscraping.com/pages/page1.html') as f:
    print(f.read())
    


"""

from urllib.request import urlopen
here, urllib is a standard python library and request is module.  urlopen is a function.


url = urlopen('https://pythonscraping.com/pages/page1.html')

print(url.read())

"""