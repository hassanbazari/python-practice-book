# print data in a csv file as a list (cutting at given symbol)
def parse(a,b,c):
	import csv
	ans=[]
        for line in open(a):
		line=line[:-1]
		ans.append(line.split(b)) 
	print ans

