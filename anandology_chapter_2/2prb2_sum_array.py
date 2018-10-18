#function to add all element of a array
def sum(num_array):
	s=0
	for num in num_array:
		try:
			s+=num
		except TypeError:
			print 'addition of '+num+ ' is not possible'
		else:			
			print 'sum is '+ str(s)





    
