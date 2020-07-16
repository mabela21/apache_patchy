#!/usr/bin/env python3

import os, sys, re
from datetime import datetime
import colorama
from colorama import Fore, Back, Style

log_file = list()

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
			if re.match(re_content, lines):
				return True

# function to find and replace lines in config files
def find_replace(file, item, new_line):
	rewritten_file = []
	re_item = r'\b' + re.escape(item) + r'\b'
	with open(file, 'r') as open_file:
		for lines in open_file:
			if re.match(re_item, lines):
				rewritten_file.append(new_line + '\n')
			else:
				rewritten_file.append(lines)
	with open(file, 'w+') as new_config:
                for lines in rewritten_file:
                        new_config.write(lines)

# function to comment, a file
def comment_settings(file, item):
        rewritten_file = []
        re_item = r'\b' + re.escape(item) + r'\b'
        with open(file, 'r') as open_file:
                for lines in open_file:
                        if re.match(re_item, lines) and '#' not in lines:
                                rewritten_file.append('#' + lines)
                        else:
                                rewritten_file.append(lines)
        with open(file, 'w+') as new_config:
                for lines in rewritten_file:
                        new_config.write(lines)

# generate a list of config files with the setting to change
def get_working_list(f_list, setting):
	working_list = list()
	for names in f_list:
		if check_file(names, setting):
			working_list.append(names)
	return working_list

# change the setting with proper function
def change_setting(w_list, setting, new_setting, set_func):
	if set_func == 'find_replace':
		for items in w_list:
			#print(items)
			find_replace(items, setting, new_setting)
			add_to_log(items, new_setting)
	elif set_func == 'uncomment':
		for items in w_list:
			print(items)
			comment_settings(items, setting)
			add_to_log(items, new_setting)
	w_list.clear()
	print('\n')

# add setting change to the log file
def add_to_log(file, new_setting):
	global log_file
	dnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	dtnow = str(dnow)
	log_line = dtnow + ': ' + file + ': ' + 'Changed setting to: ' + new_setting
	return log_file.append(log_line)

# create a rule if it does not exist in any conf files
def create_rule(bestprac, file):
	file_str = file.pop()
	with open(file_str, 'a+') as new_config:
		new_config.write(bestprac + '\n')
	add_to_log(file_str, bestprac)
	print('\n')

# prompt user to make change to settings
def user_prompt_settings(setting, url, new_setting):
	print(f'{setting}: ' + Fore.YELLOW + 'Do you want to change setting to: ' + Fore.CYAN + f'{new_setting}' + '\n' + Style.RESET_ALL + url)
	yes_no = input('Would you like to change this setting?' + Fore.CYAN + ' [Y/n]: ' + Style.RESET_ALL)
	while yes_no != 'Y' and yes_no != 'y' and yes_no != 'N' and yes_no != 'n':
		yes_no = input('Would you like to change this setting? ' + Fore.CYAN + '[Y/n]: ' + Style.RESET_ALL)
	if yes_no == 'Y' or yes_no == 'y':
		return True
	elif yes_no == 'N' or yes_no == 'n':
		return False


def main():

	print("\n\n\n")
	print(Fore.CYAN + " ______     ______   ______     ______     __  __     ______        ______     __         __  __     ______    " + Style.RESET_ALL)
	print(Fore.BLUE + "/" + Fore.CYAN + "\  __ \   " + Fore.BLUE + "/" + Fore.CYAN + "\  == \ " + Fore.BLUE + "/" + Fore.CYAN + "\  __ \   " + Fore.BLUE + "/" + Fore.CYAN + "\  ___\   " + Fore.BLUE + "/" + Fore.CYAN + "\ \_\ \   " + Fore.BLUE + "/" + Fore.CYAN + "\  ___\      " + Fore.BLUE + "/" + Fore.CYAN + "\  == \   " + Fore.BLUE + "/" + Fore.CYAN + "\ \       " + Fore.BLUE + "/" + Fore.CYAN + "\ \\" + Fore.BLUE + "/" + Fore.CYAN + "\ \   " + Fore.BLUE + "/" + Fore.CYAN + "\  ___\   ")
	print(Fore.BLUE + "\ " + Fore.CYAN + "\  __ \  " + Fore.BLUE + "\ " + Fore.CYAN + "\  _-/ " + Fore.BLUE + "\ " + Fore.CYAN + "\  __ \  " + Fore.BLUE + "\ " + Fore.CYAN + "\ \____  " + Fore.BLUE + "\ " + Fore.CYAN + "\  __ \  " + Fore.BLUE + "\ " + Fore.CYAN + "\  __\      " + Fore.BLUE + "\ " + Fore.CYAN + "\  __<   " + Fore.BLUE + "\ " + Fore.CYAN + "\ \____  " + Fore.BLUE + "\ " + Fore.CYAN + "\ \_\ \  " + Fore.BLUE + "\ " + Fore.CYAN + "\  __\   ")
	print(Fore.BLUE + " \ " + Fore.CYAN + "\_\ \_\  " + Fore.BLUE + "\ " + Fore.CYAN + "\_\    " + Fore.BLUE + "\ " + Fore.CYAN + "\_\ \_\  " + Fore.BLUE + "\ " + Fore.CYAN + "\_____\  " + Fore.BLUE + "\ " + Fore.CYAN + "\_\ \_\  " + Fore.BLUE + "\ " + Fore.CYAN + "\_____\     " + Fore.BLUE + "\ " + Fore.CYAN + "\_____\  " + Fore.BLUE + "\ " + Fore.CYAN + "\_____\  " + Fore.BLUE + "\ " + Fore.CYAN + "\_____\  " + Fore.BLUE + "\ " + Fore.CYAN + "\_____\ ")
	print(Fore.BLUE + "  \/_/\/_/   \/_/     \/_/\/_/   \/_____/   \/_/\/_/   \/_____/      \/_____/   \/_____/   \/_____/   \/_____/ " + Style.RESET_ALL)
	
	print("\n\n\n\nThank you for using " + Fore.CYAN + "apache_blue! " + Style.RESET_ALL + "Your Apache config files are now being scanned to find settings that can be changed to make your server more secure.\nWe will let you know what the best practice settings are below:\n\n")

	# directroy of apache config files
	directory = sys.argv[1]
	# find all config files
	file_list = conf_files(directory)

	# Server Tokens setting
	setting = 'ServerTokens'
	bp_setting = 'ServerTokens Prod'
	url = Fore.GREEN + 'For more info see --> [20] ' + Style.RESET_ALL + 'at https://apache-blue.gitbook.io/guide/info-leakage'
	ch_setting_func = 'find_replace'
	user_change = user_prompt_settings(setting, url, bp_setting)
	if user_change:
		working_list = get_working_list(file_list, setting)
		if not working_list:
			for x in file_list:
				if 'apache2.conf' in x:
					working_list.append(x)
					create_rule(bp_setting, working_list)
		else:
			change_setting(working_list, setting, bp_setting, ch_setting_func)
		working_list.clear()
	else:
		print('\n')

	# Server signature setting
	setting = 'ServerSignature'
	bp_setting = 'ServerSignature Off'
	url = Fore.GREEN + 'For more info see --> [21] ' + Style.RESET_ALL + 'at https://apache-blue.gitbook.io/guide/info-leakage'
	ch_setting_func = 'find_replace'
	user_change = user_prompt_settings(setting, url, bp_setting)
	if user_change:
		working_list = get_working_list(file_list, setting)
		if not working_list:
			for x in file_list:
				if 'apache2.conf' in x:
					working_list.append(x)
					create_rule(bp_setting, working_list)
		else:
			change_setting(working_list, setting, bp_setting, ch_setting_func)
		working_list.clear()
	else:
		print('\n')

	# Keep Alive setting
	setting = 'KeepAlive'
	bp_setting = 'KeepAlive On'
	url = Fore.GREEN + 'For more info see --> [24] ' + Style.RESET_ALL + 'at https://apache-blue.gitbook.io/guide/dos-attacks'
	ch_setting_func = 'find_replace'
	user_change = user_prompt_settings(setting, url, bp_setting)
	if user_change:
		working_list = get_working_list(file_list, setting)
		if not working_list:
			for x in file_list:
				if 'apache2.conf' in x:
					working_list.append(x)
					create_rule(bp_setting, working_list)
		else:
			change_setting(working_list, setting, bp_setting, ch_setting_func)
		working_list.clear()
	else:
		print('\n')

	# ETag settings
	setting = 'FileETag'
	bp_setting = 'FileETag None'
	url = Fore.GREEN + 'For more info see --> [22] ' + Style.RESET_ALL + 'at https://apache-blue.gitbook.io/guide/info-leakage'
	ch_setting_func = 'find_replace'
	user_change = user_prompt_settings(setting, url, bp_setting)
	if user_change:
		working_list = get_working_list(file_list, setting)
		if not working_list:
			for x in file_list:
				if 'apache2.conf' in x:
					working_list.append(x)
					create_rule(bp_setting, working_list)
		else:
			change_setting(working_list, setting, bp_setting, ch_setting_func)
		working_list.clear()
	else:
		print('\n')

	# Timeout settings
	setting = 'Timeout'
	bp_setting = 'Timeout <TIME IN SECONDS> [Ideal setting is 10 or less]'
	url = Fore.GREEN + 'For more info see --> [23] ' + Style.RESET_ALL + 'at https://apache-blue.gitbook.io/guide/dos-attacks'
	ch_setting_func = 'find_replace'
	user_change = user_prompt_settings(setting, url, bp_setting)
	if user_change:
		working_list = get_working_list(file_list, setting)
		user_def = input('Enter new Timeout setting' + Fore.CYAN + ' (in # of seconds): ' + Style.RESET_ALL)
		bp_setting = 'Timeout ' + user_def
		change_setting(working_list, setting, bp_setting, ch_setting_func)
		working_list.clear()
	else:
                print('\n')

	# Max Keep Alive Requests
	setting = 'MaxKeepAliveRequests'
	bp_setting = 'MaxKeepAliveRequests 100'
	url = Fore.GREEN + 'For more info see --> [25] ' + Style.RESET_ALL + 'at https://apache-blue.gitbook.io/guide/dos-attacks'
	ch_setting_func = 'find_replace'
	user_change = user_prompt_settings(setting, url, bp_setting)
	if user_change:
		working_list = get_working_list(file_list, setting)
		if not working_list:
			for x in file_list:
				if 'apache2.conf' in x:
					working_list.append(x)
					create_rule(bp_setting, working_list)
		else:
			change_setting(working_list, setting, bp_setting, ch_setting_func)
		working_list.clear()
	else:
		print('\n')

	# Keep Alive Timeout
	setting = 'KeepAliveTimeout'
	bp_setting = 'KeepAliveTimeout <TIME IN SECONDS> [Ideal setting is 15 or less]'
	url = Fore.GREEN + 'For more info see --> [26] ' + Style.RESET_ALL + 'at https://apache-blue.gitbook.io/guide/dos-attacks'
	ch_setting_func = 'find_replace'
	user_change = user_prompt_settings(setting, url, bp_setting)
	if user_change:
		working_list = get_working_list(file_list, setting)
		user_def = input('Enter new KeepAliveTimeout setting' + Fore.CYAN + ' (in # of seconds): ' + Style.RESET_ALL)
		bp_setting = 'KeepAliveTimeout ' + user_def
		change_setting(working_list, setting, bp_setting, ch_setting_func)
		working_list.clear()
	else:
                print('\n')

	# Disable WebDav Module
	#setting = 'LoadModule dav_'
	#bp_setting = 'Disable WebDav Modules'
	#url = 'PLACEHOLDER'
	#ch_setting_func = 'uncomment'
	#user_change = user_prompt_settings(setting, url, bp_setting)
	#if user_change:
	#	working_list = get_working_list(file_list, setting)
	#	change_setting(working_list, setting, bp_setting, ch_setting_func)
	#	working_list.clear()

	# Disable Trace enable
	setting = 'TraceEnable'
	bp_setting = 'TraceEnable Off'
	url = Fore.GREEN + 'For more info see --> [17] ' + Style.RESET_ALL + 'at https://apache-blue.gitbook.io/guide/attack-surface'
	ch_setting_func = 'find_replace'
	user_change = user_prompt_settings(setting, url, bp_setting)
	if user_change:
		working_list = get_working_list(file_list, setting)
		if not working_list:
			for x in file_list:
				if 'apache2.conf' in x:
					working_list.append(x)
					create_rule(bp_setting, working_list)
		else:
			change_setting(working_list, setting, bp_setting, ch_setting_func)
		working_list.clear()
	else:
		print('\n')

	# Set log level
	setting = 'LogLevel'
	bp_setting = 'LogLevel notice core:info'
	#bp_setting = 'LogLevel notice core:info'
	url = Fore.GREEN + 'For more info see --> [18] ' + Style.RESET_ALL + 'at https://apache-blue.gitbook.io/guide/logs'
	ch_setting_func = 'find_replace'
	user_change = user_prompt_settings(setting, url, bp_setting)
	if user_change:
		working_list = get_working_list(file_list, setting)
		if not working_list:
			for x in file_list:
				if 'apache2.conf' in x:
					working_list.append(x)
					create_rule(bp_setting, working_list)
		else:
			change_setting(working_list, setting, bp_setting, ch_setting_func)
		working_list.clear()
	else:
		print('\n')

	# Limit Requestline
	setting = 'LimitRequestline'
	bp_setting = 'LimitRequestline 512'
	url = Fore.GREEN + 'For more info see --> [29] ' + Style.RESET_ALL + 'https://apache-blue.gitbook.io/guide/bof-attacks'
	ch_setting_func = 'find_replace'
	user_change = user_prompt_settings(setting, url, bp_setting)
	if user_change:
		working_list = get_working_list(file_list, setting)
		if not working_list:
			for x in file_list:
				if 'apache2.conf' in x:
					working_list.append(x)
					create_rule(bp_setting, working_list)
		else:
			change_setting(working_list, setting, bp_setting, ch_setting_func)
		working_list.clear()
	
	dnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	dtnow = str(dnow)
	log_name = dtnow + "_apache_blue.log"
	# write the log file
	with open(log_name, 'w+') as final_log:
		for events in log_file:
			final_log.write(events + '\n')

	print(f"\n\n\nLooks like you're all set! To review the settings that were changed, please see " + Fore.GREEN + f"./{log_name}" + Style.RESET_ALL)
	print(Fore.CYAN + "\nFor more information about hardening Apache servers, visit https://apache-blue.gitbook.io/guide" + Style.RESET_ALL)
	print("\nThanks again for using " + Fore.CYAN + "apache_blue. " + Style.RESET_ALL + "Have a great day!\n\n")

if __name__ == "__main__":
	main()
