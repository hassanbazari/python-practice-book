def check_case(str1,str2):
	if str1.islower():
		x=str1
	else:
		x=str1.lower()
	if str2.islower():
		y=str1
	else:
		y=str1.lower()
	if x==y:
		print(True)
	else:
		print(False)
#function 2 words are same irrespective of cases.			
def istrcmp(str1,str2):
	if len(str1)==len(str2):
		check_case(str1,str2)
	else:
		print(False)

