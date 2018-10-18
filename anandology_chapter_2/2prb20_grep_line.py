#program to print a line with specific word with 'grep' unix cammand
import sys
import os
filename = sys.argv[1]
word=sys.argv[2]
cammand= 'grep -n "'+word+ '" '+filename
print os.system(cammand)

