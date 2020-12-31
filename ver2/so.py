import requests
from bs4 import BeautifulSoup

def getLastPage(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    pages = pages[0:-1]
    maxPage = pages[-1].get_text(strip = True)
    
    return int(maxPage)

def extractJob(html):
    title = html.find("h2", {"class":"mb4"}).find("a")["title"]
    company, location = html.find("h3", {"class":"mb4"}).find_all("span",recursive=False)
    #unpacking value
    company = company.get_text(strip=True).strip("\n")
    location = location.get_text(strip=True).strip("-").strip("\n")
    jobId = html['data-jobid']

    return {'title':title, 'company':company, 'location':location, 'link':f"https://stackoverflow.com/jobs/{jobId}"}

def extractJobs(lastPage,URL):
    jobs = []

    for page in range(lastPage):
        print(f"Scrapping StackOverflow: Page: {page+1}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extractJob(result)
            jobs.append(job)   

    return jobs

def getJobs(word):
    URL=f"https://stackoverflow.com/jobs?q={word}"
    lastPage = getLastPage(URL)
    jobs=extractJobs(lastPage,URL)
    return jobs