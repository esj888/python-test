import fileinput
from bs4 import BeautifulSoup


with open("website.html", encoding="utf8") as page:
    page_data = page.read()
    print(page_data)

soup = BeautifulSoup(page_data, "html.parser")
print(soup.title)
# print(soup.prettify())
print(type(soup))
print(soup.p)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")  # need to use class_ not class
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")  # css selector
print(name)

headings = soup.select(".heading")  # css selector
print(headings)
