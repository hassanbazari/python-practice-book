#function to print strings in a list in increase in order of length
def lensort(string_array):
	for i in range(len(string_array)):
		if type(string_array[i])==int:
			string_array[i]=str(string_array[i])
	ans=[]
	for i in sorted(string_array, key=len, reverse=False):
		ans.append(i)
	print ans
