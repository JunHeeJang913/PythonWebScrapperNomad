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

def extractIndeedJobs(lastPages):
    jobs = []
    for page in range(lastPages):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)
    return jobs