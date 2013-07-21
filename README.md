site-sonar
==========

## An Automated Site-Active Checker ##

Every client thinks they're the center of the universe, but as developers we can't afford to sit around and click "refresh" on every live site we've deployed. site-sonar is a simple tool to allow you to automatically ping a URL and verify that it is active.

### Usage ###
Input - A list of urls to check (uses default settings)
<pre>
$ python main.py http://sleeplesshacker.com http://sleeplesshacker.com/non-existent-page
Failed URLs:
http://sleeplesshacker.com/non-existent-page
$ 
</pre>

Input - A YAML file specifying custom settings to be checked on each page
<pre>
$ python main.py -f ../testfile.yaml
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
  url: "http://sleeplesshacker.com/non-existent-url",
  status_code: 200
 },
 {
  url: "http://sleeplesshacker.com/non-existent-url-404",
  status_code: 404
 }
]
</pre>

