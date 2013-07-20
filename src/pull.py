import requests

urls = ['http://sleeplesshacker.com', 'http://sleeplesshacker.com/non-existent-page']

failures = []

for page in urls:
	r = requests.get(page)
	if r.status_code != 200:
		failures.append(page)

if len(failures) > 0:
	print "Failed URLs"
	for f in failures:
		print f

