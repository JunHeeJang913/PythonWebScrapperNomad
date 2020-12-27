from indeed import getJobs as getIndeedJobs
from so import getJobs as getSoJobs
from save import saveToFile

def getJobs(word):
    soJobs = getSoJobs(word)
    indeedJobs = getIndeedJobs(word)
    jobs = soJobs+indeedJobs

    return jobs
#CSV comma seperated value

saveToFile(jobs)