#function to print words with same alphabets in a list
def anagrams(list1):
	words=[]
	ans=[]
	for word in list1:
		words=words+[''.join(sorted(word))]
		num_anagrams=set(words)
	for word in num_anagrams:
		same_words=[]
		for same_word in list1:
			if word ==''.join(sorted(same_word)):
				same_words.append(same_word)
		ans.append(same_words)
	print(ans)
