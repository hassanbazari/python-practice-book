#function to find cumulative sum of a list
def cumulative_sum(num_array):
	sum_list=[]
	ans=0
	for element in num_array:
		if type(element)==int:
			ans=ans+element
			sum_list.append(ans)
		else:
			sum_list=sum_list+['addition not possible']
	print 'ARRAY: ',sum_list

