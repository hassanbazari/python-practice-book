#function to find duplicated elements in a list
def dups(num_array):
	ans=[]
	duplicate=[]
	for i in range(len(num_array)):
		if num_array[i] in num_array[i+1:]:
			ans.append(num_array[i])
		else:
			pass
	duplicate=set(ans)
	ans=list(duplicate)
	print(ans)
			



