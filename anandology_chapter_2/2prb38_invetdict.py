#function to change key to value and value to key
def invertdict(dictionary):
	inv_dictionary = {v: k for k, v in dictionary.iteritems()}
	print inv_dictionary
