import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL=f"https://www.indeed.com/jobs?q=python&limit={LIMIT}&radius=25"

def extractIndeedPages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div",{"class":"pagination"})

    links = pagination.find_all('a')

    pages = []

    for link in links[:-1]:
        pages.append(int(link.find("span").string))

    maxPage = pages[-1]

    return maxPage

def extractJobs(html):
    title = html.find("h2",{"class":"title"}).find("a")["title"]
    company = html.find("span",{"class":"company"})

    if company.find("a") is not None:
        company = str(company.find("a").string)
    else:
        company = str(company.string)

    company = company.strip() 

    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]

    jobId=html["data-jk"]

    return {'title':title,'company':company, 'location':location, "link":f"https://www.indeed.com/viewjob?jk={jobId}"}

def extractIndeedJobs(lastPages):    
    jobs = []

    for page in range(lastPages):
        print(f"Scrapping Indeed: Page: {page+1}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
        for result in results:
            job = extractJobs(result)
            jobs.append(job)

    return jobs

def getJobs():
    lastPages = extractIndeedPages()

    jobs=extractIndeedJobs(lastPages)

    return jobs