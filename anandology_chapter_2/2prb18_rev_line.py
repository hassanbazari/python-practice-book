# program to print each line in reversed order
lines = []
import sys
name = sys.argv[1]
with open(name) as f:
	lines = f.readlines()
for line in lines:
        line=line[:-1]
	print(line[::-1])
        
