import fileinput
from bs4 import BeautifulSoup


with open("website.html", encoding="utf8") as page:
    page_data = page.read()
    print(page_data)

soup = BeautifulSoup(page_data, "html.parser")
print(soup.title)
print(type(soup))


