#!/usr/bin/env python3

import os, sys

def conf_files(path):
    config_files = list()
    for pd, directories, files in os.walk(path):
        for file in files:
            if file.endswith('.conf'):
            	fname = os.path.join(pd, file)
            	config_files.append(fname)
    return config_files 

def check_file(file, content):
	with open(file, 'r') as x:
		for lines in x:
			if content in lines:
				return True
  
directory = sys.argv[1]
file_list = conf_files(directory)
print(file_list)
for names in file_list:
	if check_file(names, 'ServerTokens'):
		print(names)

	