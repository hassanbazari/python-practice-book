# program to print bottom to top of given file 
import sys
name = sys.argv[1]
lines = []
with open(name) as f:
	lines = f.readlines()
for line in reversed(lines):
        print (line[:-1])
        
