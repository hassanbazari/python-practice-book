# function to sort list of file according to extension
def extsort(file_list):
	ans=[]
	extension=[]
#-------------extract the extension from filename----------# 
	for file in file_list:
		extension=extension+[file.split(".")[-1]]
	extension=list(set(extension))		
	extension.sort()						#sort extension
	file_list.sort()						#sort list
	for ext in extension:						#print list according sorted extension
		same_ext =[ x for x in file_list  if ext in x]
		ans.append(same_ext)
	ans = [item for sublist in ans for item in sublist]
	print ans 
