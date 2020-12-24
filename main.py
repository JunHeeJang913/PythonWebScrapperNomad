import requests
from bs4 import BeautifulSoup

indeedResult = requests.get("https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

indeedSoup = BeautifulSoup(indeedResult.text, "html.parser")

pagination = indeedSoup.find("div",{"class":"pagination"})

links = pagination.find_all('a')

pages = []

for link in links[:-1]:
    pages.append(int(link.find("span").string))

maxPage = pages[-1]