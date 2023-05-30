import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
r = requests.get(url)
html_content = r.text

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())

#--
title = soup.title.string
print('Title:', title)

paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.get_text())


#--
header_tags = soup.find_all('h2', class_='header-class')
for header in header_tags:
    print(header.get_text())

#--
main_content = soup.find(id='main-content')
print(main_content.get_text())

#--
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
