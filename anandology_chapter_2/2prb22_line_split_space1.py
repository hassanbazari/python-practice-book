import sys,re
filename = sys.argv[1]
Size=sys.argv[2]
size=int(Size)
lines = []
with open(filename) as f:
	lines = f.readlines()						#read all lines
for line in lines:
	line=line[:-1]+' '						#remove newline and add space at end
	spaces=[m.start() for m in re.finditer(' ', line)]		#find spaces in the line
	cutline=[0]							#add zero to get beginning of the line
	x=0
	#---------find cutting space positions in the line----------------#
	for element in spaces:
		if (element-x)/size>0:
			cutline=cutline+[element+1]		#add 1 to element to avoid space at the begining  of line
			x=element
		else:
			pass
	#----------print lines at cutting positions-----------------------#
	for pos in range(len(cutline)-1):
		start=cutline[pos]
		end=cutline[pos+1]
		print line[start:end]
		
		
	
