import os.path
import urllib2
import sys
s=sys.argv[1]
if (s[len(s)-1]=='/'):
	response = urllib2.urlopen(s)
	print ("saving  " +s+" as intex.html")
else:
	y=os.path.basename(s)
	response = urllib2.urlopen(s)
	print ("saving  " +s+" as "+ y)

