def make_slug(string):
	import re
	string = re.sub(r'[^\w\s]','',string)		#remove punchuations
	string=re.sub("\s\s+", " ", string)		#remove multiplespace
	string = string.strip()				#remove space in front and end
	string=string.replace(" ", "-")			
	print string

