import csv

def saveToFile(jobs):
    file = open("jobs.csv", mode = "w",encoding='UTF-8')     #w:write
    writer = csv.writer(file)
    writer.writerow(["title", "commpany", "location", "apply_link"])

    for job in jobs:
        writer.writerow(list(job.values()))