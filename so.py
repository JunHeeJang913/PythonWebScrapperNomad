import requests
from bs4 import BeautifulSoup

URL=f"https://stackoverflow.com/jobs?q=python"

def getLastPage():
    result = requests.get(URL)
    soup = BeautifulSoup.(result.txt, "html.parser")
    pages = soup.find("div", {"class":"pagination"}).find_all("a")
    maxPage = pages[-1]
    
    return maxPage


    

def getJobs():
    lastPages = getLastPage()

    jobs=extractJobs(lastPages)

    return jobs