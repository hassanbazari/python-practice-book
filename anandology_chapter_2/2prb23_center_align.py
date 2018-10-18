#program to print the text in a file center alligned format
import sys
name = sys.argv[1]
with open(name) as f:
	for line in f:
		tot_space=50-(len(line[:-1]))
		front_space=tot_space/2
		z=' '*front_space
            	print (z+line[:-1])
