# function to split data in a file into words and print in decresing order of occurences 
def read_words(filename):
	sorted_dict={}
	import re
	from collections import Counter 
	import operator      
	words = re.findall(r'\w+', open(filename, 'r').read().lower())			#list of words without punchuation
	dictionary=Counter(words)							#take count each word and arrange in descending order
	
