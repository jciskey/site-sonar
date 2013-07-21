import argparse #Commandline options
import yaml #Specification-file
import pull #Main functionality
import sys

#Commandline options
parser = argparse.ArgumentParser(description='site-sonar, a tool for automatically checking if sites are active')
parser.add_argument('url', help='A url to check with default settings. Either this argument must be given, or the -f flag must be used.', nargs='*')
parser.add_argument('-f','--file', help='Used to specify a file of sites to check. Either this flag must be used, or the url argument must be used.')
args = vars(parser.parse_args())

#Pull the list of sites to be checked, depending on how the user specified them
urls = []
if args['url']:
	for x in args['url']:
		urls.append({url: x})
elif args['file']:
	sites_file = open(args['file'], 'r')
	settings = yaml.safe_load(sites_file)
	for site in settings:
		urls.append(site)
else:
	parser.print_help()
	sys.exit(1)

#Check each site
failures = []
for page in urls:
	if not pull.page_alive(page):
		failures.append(page['url'])

#Print failures
if len(failures) > 0:
	print "Failed URLs:"
	for f in failures:
		print f

