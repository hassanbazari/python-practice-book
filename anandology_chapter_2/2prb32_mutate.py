mutant_list=[]
def add (word):
	mutant_list.append(''.join(word))
	return mutant_list

def mutate(Word):
	import string
	ans=[]	
	for i in range(len(Word)):
		#mutant with one letter less
		word=list(Word)	
		del word[i]			
		ans=add(word)
	#---------------------------------------------------
		#mutant with alphabet substitution
		alphabet=list(string.ascii_lowercase)+list(string.ascii_uppercase)
		for j in alphabet:
			word=list(Word)	
			word[i]=j
			ans=add(word)
	#--------------------------------------------------- 
	#mutant with position change
	for i in range(len(Word)):
		for j in range(len(Word)):
			word=list(Word)
			x=word[i]
			word[i]=word[j]
			word[j]=x
			ans=add(word)
	return ans




