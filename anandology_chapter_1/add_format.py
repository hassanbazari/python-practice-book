#receive 2 values argument and add them print in format
import sys
number1= sys.argv[1]
number2= sys.argv[2]
try:
	sum=int(number1)+int(number2)
	print(number1+'+'+number2+'='+str(sum))
except ValueError:
	print ('Enter integer value ') 

