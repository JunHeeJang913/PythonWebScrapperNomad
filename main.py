from indeed import getJobs as getIndeedJobs
from so import getJobs as getSoJobs
from save import saveToFile

soJobs = getSoJobs()
indeedJobs = getIndeedJobs()

jobs = soJobs+indeedJobs
#CSV comma seperated value

saveToFile(jobs)