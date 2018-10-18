#function to check whether the file contain c or python program
def file_identify(filename):
	with open(filename) as f:
		lines = f.readlines()
	for line in lines:
		if line[-2]==';':
			print filename + '  is a C file'
		else:
			print filename + '  is a python file'
