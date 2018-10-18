#program to slice the line in a text file at a specific size
import sys
filename = sys.argv[1]
Size=sys.argv[2]
size=int(Size)
lines = []
with open(filename) as f:
	lines = f.readlines()
for line in lines:
	splitline = [line[i:i+size] for i in range(0, len(line), size)]		#split line at specific size
	x=splitline[-1]								# select the last piece of list
	splitline[-1]=x[:-1]							#remove \n at the end
	for i in splitline:
		print (i)
