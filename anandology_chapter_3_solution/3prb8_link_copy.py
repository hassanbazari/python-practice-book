import urllib2
import sys
from bs4 import BeautifulSoup
url = sys.argv[1]
conn = urllib2.urlopen(url)
html = conn.read()
soup = BeautifulSoup(html)
links = soup.find_all('a')
for tag in links:
    link = tag.get('href',None)
    if link is not None:
        print link
