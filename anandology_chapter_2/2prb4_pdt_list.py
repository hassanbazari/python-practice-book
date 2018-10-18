#product of elements in a list
def product(num_array):
	ans=1
	for element in num_array:
		if type(element)==int:
			ans=ans*element
		else:
			print 'multiplication of '+element+ ' is not possible'
	print 'product is '+ str(ans)
	

