# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

page=requests.get('https://www.michigandaily.com/about/archive')

status=page.status_code

headers=page.headers


content=page.content

soup=BeautifulSoup(content, 'html.parser')

find_a=soup.find_all('a', href = True)

top_articles=find_a[18:23]

print('Michigan Daily -- MOST READ')

for a in top_articles:
    href=a['href']
    link="http://www.michigandaily.com" + str(href)
    article=requests.get(link)
    info=article.content
    beauty=BeautifulSoup(info, 'html.parser')
    find_a_2=beauty.find("div", {"class" : "link"})
    find_p= beauty.find("p",{"class": "info"})
    title= a.get_text()
    print(title)
    try:
        author=find_a_2.get_text()
        print('  by ' + author)
    except AttributeError:
        anonymous = find_p.get_text()[3:21]
        print('  by ' + anonymous)
