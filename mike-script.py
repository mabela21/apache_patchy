#!/usr/bin/env python3

import os, sys, re

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
	re_content = r'\b' + content + r'\b'
	with open(file, 'r') as x:
		for lines in x:
			if re.match(re_content, lines): #and '#' not in lines:
				return True

# function to find and replace lines in config files
def find_replace(file, item, new_line):
	rewritten_file = []
	re_item = r'\b' + re.escape(item) + r'\b'
	with open(file, 'r') as open_file:
		for lines in open_file:
			if re.match(re_item, lines): #and '#' not in lines:
				rewritten_file.append(new_line + '\n')
			else:
				rewritten_file.append(lines)
	with open(file, 'w+') as new_config:
                for lines in rewritten_file:
                        new_config.write(lines)

def get_working_list(f_list, setting):
	working_list = list()
	for names in f_list:
		if check_file(names, setting):
			working_list.append(names)
	return working_list

def change_setting(w_list, setting, new_setting):
	for items in w_list:
		print(items)
                #print(find_replace(items, 'ServerTokens', 'ServerTokens Prod'))
		find_replace(items, setting, new_setting)
	w_list.clear()

def main():
	# directroy of apache config files
	directory = sys.argv[1]
	# find all config files
	file_list = conf_files(directory)
	# a list that will keep track of files with different config settings
	#working_list = list()
	#print(file_list)

	# Server Tokens setting
	working_list = get_working_list(file_list, 'ServerTokens')
	#print(working_list)
	change_setting(working_list, 'ServerTokens', 'ServerTokens Prod')
	working_list.clear()

	# Server signature setting
	working_list = get_working_list(file_list, 'ServerSignature')
	change_setting(working_list, 'ServerSignature', 'ServerSignature Off')
	working_list.clear()

	# Keep Alive setting
	working_list = get_working_list(file_list, 'KeepAlive')
	change_setting(working_list, 'KeepAlive', 'KeepAlive On')
	working_list.clear()

	# ETag settings
	working_list = get_working_list(file_list, 'FileETag')
	change_setting(working_list, 'FileETag', 'FileEtag None')
	working_list.clear()

	# Timeout settings
	working_list = get_working_list(file_list, 'Timeout')
	user_def = input('Enter an amount of Timeout setting in seconds: ')
	change_setting(working_list, 'Timeout', 'Timeout ' + user_def)
	working_list.clear()

# may want to make zero
	# Max Keep Alive Requests
	working_list = get_working_list(file_list, 'MaxKeepAliveRequests')
	change_setting(working_list, 'MaxKeepAliveRequests', 'MaxKeepAliveRequests 0')
	working_list.clear()

	# Keep Alive Timeout
	working_list = get_working_list(file_list, 'KeepAliveTimeout')
	user_def = input('Enter Keep ALive Timeout setting: ')
	change_setting(working_list, 'KeepAliveTimeout', 'KeepAliveTimeout ' + user_def)
	working_list.clear()

if __name__ == "__main__":
	main()