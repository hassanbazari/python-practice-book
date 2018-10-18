def zip(list1,list2):
	ans=[]
	if len(list1)>=len(list2):
		for i in range(len(list1)):
			ans=ans+[(list1[i],list2[i])]
	else:
		for i in range(len(list2)):
			ans=ans+[(list1[i],list2[i])]
	print ans
