from indeed import extractIndeedPages, extractIndeedJobs

lastIndeedPages = extractIndeedPages()

indeedJobs=extractIndeedJobs(lastIndeedPages)

print(indeedJobs)