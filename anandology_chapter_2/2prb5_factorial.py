# function to find factorial of a number
def factorial(num):
	if type(num)==int:
		ans=1
		count=1
		while count <= num : 
			ans=ans*count
			count=count+1
		print ans
	else:
		print ("Enter a integer number")
