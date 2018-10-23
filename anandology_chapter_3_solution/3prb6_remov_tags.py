import urllib
import sys
import re
name = sys.argv[1]
htmlfile=urllib.urlopen(name)
htmltext=htmlfile.read()
cleanr = re.compile('<.*?>')
cleantext = re.sub(cleanr, '',htmltext)
print cleantext

