#print triplets in the list whose sum of any two element gives 3rd element
def triplets(num):
	print[(x, y,z) for x in range(1,num) for y in range(x,num) for z in range(1,num) if (x+y) == z]













