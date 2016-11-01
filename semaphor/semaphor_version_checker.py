from urllib import urlopen
from bs4 import BeautifulSoup
import re

semaphor_version_site = urlopen('https://spideroak.com/semaphor/versioncheck/1.1.7/linux/x64').read()
output = BeautifulSoup(semaphor_version_site, "html.parser")
versioninfo = output.find('div', 'cms-ribbon columns-one-ribbon versioncheck')
for check in output.findAll('p', attrs={'class':'red'}):
    if "not the current version" in check.text:
        print "New version available"

