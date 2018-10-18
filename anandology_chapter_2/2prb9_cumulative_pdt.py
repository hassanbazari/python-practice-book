def cumulative_product(num_array):
	pdt_list=[]
	ans=1
	for element in num_array:
		if type(element)==int:
			ans=ans*element
			pdt_list.append(ans)
		else:
			pdt_list=pdt_list+['multiplication not possible']
	print 'ARRAY: ',pdt_list







