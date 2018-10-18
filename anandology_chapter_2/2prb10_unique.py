#function to find unique element in list without using set
def unique(in_list):
	out_list=[]
	for element in in_list:		
		if element in out_list:
			pass
		else:
			out_list=out_list+[element]
	print out_list
