import re, urllib.request
from bs4 import BeautifulSoup

all_links = []
all_names = []

url_first_part = 'http://python-data.dr-chuck.net/known_by_'
url_last_part = '.html'
first_entry = 'Jarl'

for i in range(7):
    url = url_first_part + first_entry + url_last_part

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    #def get_next_name(url)
    tags = soup('a')
    links = []
    for tag in tags:
        links.append(tag.get('href', None))
    url = links[17]
    print (url)

    name = url[41:]
    next_entry = name[:-5]
    all_names.append(next_entry)
    first_entry = next_entry
    url = url_first_part + first_entry + url_last_part
    all_links.append(url)
    print (all_names[-1])
