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

def extractJob(html):
    title = html.find("find", {"class":"-title"}).find("h2").find("a")["title"]
    company, location = html.find("div", {"class":"-company"}).find_all("span",recursive=False)
    #unpacking value
    company = company.get_text(strip=True).strip("\n")
    location = company.get_text(strip=True).strip("-").strip("\n").strip(" \r")

    return {'title':title, 'company':company, 'location':location}

def extractJobs(lastPage):
    jobs = []

    for page in range(lastPage):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extractJob(result)
            jobs.append(job)   

    return jobs

def getJobs():
    lastPage = getLastPage()

    jobs=extractJobs(lastPage)

    return jobs