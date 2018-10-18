# print data in a csv file as a list
def parse_csv(a):
	import csv
	ans=[]
        for line in open(a):
		line=line[:-1]
		ans.append(line.split(',')) 
	print ans

