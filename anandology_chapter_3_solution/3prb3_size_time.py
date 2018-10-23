import sys
import os
import time
directory=sys.argv[1]
file_list = os.listdir(directory)
print "FILENAME		SIZE	MODIFIED DATE"
for files in file_list:
	b=directory+'/'+files
	size=str(os.stat(b).st_size)
	Time=time.ctime(os.path.getmtime(b))
	print (files+"		"+size+"	"+Time)
