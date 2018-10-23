def file_list(file):
	from os import listdir
	from os.path import isfile, join
	files_list = [f for f in listdir(file) if isfile(join(file, f))]
	print(files_list);


