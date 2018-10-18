#function to print unique element in list according to condition
def unique(in_list , key=lambda s: s.lower()):
	out_list=[]
	in_list=[key(x) for x in in_list]
	for element in in_list:		
		if element in out_list:
			pass
		else:
			out_list=out_list+[element]
	print out_list
