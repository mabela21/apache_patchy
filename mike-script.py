#!/usr/bin/env python3

import os, sys

# find all config files
def conf_files(path):
    config_files = list()
    for pd, directories, files in os.walk(path):
        for file in files:
            if file.endswith('.conf'):
            	fname = os.path.join(pd, file)
            	config_files.append(fname)
    return config_files

# check config file for a setting
def check_file(file, content):
	with open(file, 'r') as x:
		for lines in x:
			if content in lines:
				return True

# function to find and replace lines in config files
def find_replace(file, item, new_line):
	rewritten_file = []
	with open(file, 'r') as open_file:
		for lines in open_file:
			if item in lines and '#' not in lines:
				rewritten_file.append(new_line + '\n')
			else:
				rewritten_file.append(lines)
	with open(file, 'w+') as new_config:
                for lines in rewritten_file:
                        new_config.write(lines)

def main():
	# directroy of apache config files
	directory = sys.argv[1]
	# find all config files
	file_list = conf_files(directory)
	# a list that will keep track of files with different config settings
	working_list = list()
	#print(file_list)
	# Server Tokens setting
	for names in file_list:
		if check_file(names, 'ServerTokens'):
			working_list.append(names)
	#print(working_list)
	for items in working_list:
		print(items)
		#print(find_replace(items, 'ServerTokens', 'ServerTokens Prod'))
		find_replace(items, 'ServerTokens', 'ServerTokens Prod')

	working_list.clear()

	# Server Signature Setting
	for names in file_list:
		if check_file(names, 'ServerSignature On'):
			working_list.append(names)
	for items in working_list:
		print(items)
		find_replace(items, 'ServerSignature On', 'ServerSignature Off')

if __name__ == "__main__":
	main()