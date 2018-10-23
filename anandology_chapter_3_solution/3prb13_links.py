import sys
link = sys.argv[1]
from bs4 import BeautifulSoup
import urllib2
resp = urllib2.urlopen(link)
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
for link in soup.find_all('a', href=True):
	print link['href']
