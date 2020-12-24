import requests
from bs4 import BeautifulSoup

URL=f"https://stackoverflow.com/jobs?q=python"

def getLastPage():
    result = requests.get(URL)
    soup = BeautifulSoup.(result.text, "html.parser")
    pages = soup.find("div", {"class":"pagination"}).find_all("a")
    pages = pages[0:-1]
    maxPage = pages[-1].get_txt(strip = True)
    
    return int(maxPage)


def extractJobs(lastPage):
    jobs = []

    for page in range(lastPage):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})


    

def getJobs():
    lastPage = getLastPage()

    jobs=extractJobs(lastPage)

    return jobs