#function to convert list to list of list of given size
def group(mother_list,size):
	new_list = [mother_list[i:i+size] for i in range(0, len(mother_list), size)]
	print (new_list)

















