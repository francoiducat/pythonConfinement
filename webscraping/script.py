import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/example.html", headers={
                 'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c = r.content

soup = BeautifulSoup(c, "html.parser")

# print(soup.prettify())

divs = soup.findAll("div", {"class": "cities"})
h2 = soup.findAll("h2")

print(divs)
print(h2)

for h in h2:
    print(h.text)

