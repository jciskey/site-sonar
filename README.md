site-sonar
==========

## An Automated Site-Active Checker ##

Every client thinks they're the center of the universe and get mad at the slightest downtime, but as developers we can't afford to sit around and click "refresh" on every site we've deployed just to make sure it's still up. site-sonar is a simple tool to allow you to automatically ping a URL and verify that it is active.

By default, site-sonar considers any response aside from a Status Code 200 to be a failure. This is normally what is desired, but it is customizable by passing in a settings file.

### Usage ###
Input - A list of urls to check (uses default settings)
<pre>
$ python site-sonar.py http://sleeplesshacker.com http://sleeplesshacker.com/non-existent-page
Failed URLs:
http://sleeplesshacker.com/non-existent-page
$ 
</pre>

Input - A YAML file specifying custom settings to be checked on each page
<pre>
$ python site-sonar.py -f ../testfile.yaml
Failed URLs:
http://sleeplesshacker.com/non-existent-url
</pre>

YAML file
<pre>
[
 {
  url: "http://sleeplesshacker.com",
  status_code: 200
 },
 {
  url: "http://sleeplesshacker.com/non-existent-url"
 },
 {
  url: "http://sleeplesshacker.com/non-existent-url-404",
  status_code: 404
 }
]
</pre>


### Requirements ###
site-sonar is developed on Python 2.7, with the following libraries:

PyYAML==3.10
argparse==1.2.1
requests==1.2.3
wsgiref==0.1.2

If you get it to work using other combinations, feel free to let me know and I'll put up a note about it.
