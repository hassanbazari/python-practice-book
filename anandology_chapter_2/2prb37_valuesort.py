#function to print value of sorted key
def valuesort(dictionary):
	ans=[]
	key=dictionary.keys()
	key.sort()
	for i in range (len(key)):
		ans.append(dictionary[key[i]])
	print ans
	
