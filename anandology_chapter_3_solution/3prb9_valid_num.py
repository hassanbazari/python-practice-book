def check(number):
	try:
		x=int(number)
		print('Valid number')
	except ValueError:
		print 'Invalid number'


def phone_num(num):
	#international phone_num format +12 1234 123456(country_code area _code subcriber_code)
	if type(num)==int :
		length=len(str(num))
		if length==10:
			print 'Enter the phone num with country code'
		else:
			print 'Invalid number'
	if type(num)== str :
		if len(str(num))==13:
			if num[0]=='+':
				number=num[1:]
				check(number)
			else:
				print 'Invalid number'
		elif len(str(num))<13:
			print 'Short in the length of number'
		else:
			print 'numberformat :+121234123456(country_code area _code subcriber_code)'
