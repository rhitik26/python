from requests import get
from bs4 import BeautifulSoup as bs
url='http://www.moneycontrol.com'
res=get(url)
soup=bs(res.text,'html.parser')
# print(type(soup))
# print(soup.html.head.title)
# print(soup.html.head.meta)
divs=soup.find_all(attrs={"id":"maNSE"})
# trs=soup.find_all('tr')
# print(trs)
for d in divs:
    tbls=d.find_all('table',class_='rhsglTbl')
    # print(tbls)
    for p in tbls:
        links=p.find_all('a')
        for l in links:
            print(l.get('title'))