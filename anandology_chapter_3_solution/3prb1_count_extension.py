import os
import sys
f=sys.argv[1]
list_file = os.listdir(f)
extension_list=[]
for files in list_file:
	extension_list.append(files.split(".")[-1])
	extensions=set(extension_list)
for extension in extensions:
	count=0
	for files in list_file:
		if extension in files:
 			count=count+1
	print count , extension
	
