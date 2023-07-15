from googlesearch import search
numberOfResults = 10
prefJob = "Electrician Jobs"
results = search(prefJob, num_results=numberOfResults)
ignoreWebsites = ['indeed', 'simplyhired', 'linkedin']
maxNumberOfLinks = 2
links = []
for _ in range(numberOfResults):
    nextResult = next(results)
    if not any(website in nextResult for website in ignoreWebsites):
        links.append(nextResult)
    if len(links) == maxNumberOfLinks:
        break
print(links[1])