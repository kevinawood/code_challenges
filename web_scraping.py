import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page)
# print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# print(list(soup.children)[2])
# print(type(item) for item in list[soup.children])
html = list(soup.children)[2]
# print(list(html.children))
body = list(html.children)[3]

print(list(body.children))
p = list(body.children)[1]

print(p.get_text())
