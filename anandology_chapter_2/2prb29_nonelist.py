#function to create list of list of None at a given size
def array(size_motherlist,size_childlist):
	print [[None for i in range(size_childlist)] for j in range(size_motherlist)]
