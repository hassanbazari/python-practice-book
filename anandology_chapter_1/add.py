#receive 2 values argument and add them
import sys
number1= sys.argv[1]
number2= sys.argv[2]
try:
	sum=int(number1)+int(number2)
	print(sum)
except ValueError:
	print ('Enter integer value ') 
