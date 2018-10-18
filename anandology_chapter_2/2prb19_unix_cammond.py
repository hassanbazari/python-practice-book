# program to print first and last 20 line of given file
import os
import sys
name = sys.argv[1]
unix_cammond1="head -20 "+name		#create unix cammond as string for print first 20 lines
unix_cammond2="tail -20 "+name		#create unix cammond as string for print last 20 lines
os.system(unix_cammond1)
os.system(unix_cammond2)

