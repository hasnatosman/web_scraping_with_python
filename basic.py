from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<title> HASNAT </title>
</head>
<body> 
<p> My name is HASNAT OSMAN </p>
<b> ScCRAP </b>
<b> Python </b>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html_doc)

soup = BeautifulSoup(html_doc, 'lxml')

# print out nicely formatted HTML
# print(soup.prettify())

# tag , bold tag,

print(soup. find_all('b'))
# print(soup.b)

print('\n')
