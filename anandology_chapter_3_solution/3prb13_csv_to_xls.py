import sys
input = sys.argv[1]
output=sys.argv[2]
from openpyxl import Workbook
import csv
wb = Workbook()
ws = wb.active
with open(input, 'r') as f:
	for row in csv.reader(f):
		ws.append(row)
wb.save(output)

