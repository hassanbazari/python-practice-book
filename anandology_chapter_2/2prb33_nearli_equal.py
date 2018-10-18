#function to check whether given words are nearly_equal
def nearly_equal(word1,word2):
	Word1=list(word1)
	Word2=list(word2)
	if len(word1)>len(word2):
		diff = [letter for letter in Word1 if letter not in Word2]
	else:
		diff = [letter for letter in Word2 if letter not in Word1]
	if len(diff)>1:
		print False
	else:
		print True

