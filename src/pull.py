import requests

default_settings = {
	'status_code': 200
}

def page_alive(url_settings):
	'''Pulls a url and returns True or False, depending on whether the response matches the passed settings.'''
	#Grab the settings, and set defaults
	#--URL to pull from
	url = url_settings['url']
	#--Status code to expect
	if ('status_code' in url_settings) and (url_settings['status_code']):
		status_code = url_settings['status_code']
	else:
		status_code = default_settings['status_code']
	
	#Pull the URL
	try:
		r = requests.get(url)
	except requests.exceptions.RequestException as e:
		return False
	
	if r.status_code != status_code:
		return False
	else:
		return True


