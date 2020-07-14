#!/usr/bin/env python3

import os

def main():

    original_conf_contents = []

    with open("ch8.conf", "r") as original_conf:
        original_conf_contents = original_conf.readlines()

    os.rename("ch8.conf", "ch8.conf.bak")

    with open("ch8.conf", "w+") as patched_conf:

        for line in original_conf_contents:

            if "ServerTokens" in line:
                if "Prod" not in line:
                    current_setting = line.replace("ServerTokens ", '').strip()
                    print(f"ServerTokens is currently set to {current_setting} which could potentially reveal Apache version and module information to hackers, allowing them to find exploits")
                    print(f"Changing {current_setting} to Prod will only display 'Apache' and will not show any version numbers")
                    print("Would you like to apply this change to make your server more secure? (Type 'no' to keep settings as they are, any other input will be interpreted as a 'yes')")
                    answer = input()
                    if answer not in ('no', 'No', 'NO'):
                        patched_conf.write("ServerTokens Prod\n")
                        print("Setting was changed\n")
                    else:
                        patched_conf.write(line)
                        print("Setting was not changed\n")
            
            elif "ServerSignature" in line:
                if "Off" not in line:
                    current_setting = line.replace("ServerSignature ", '').strip()
                    print(f"ServerSignature is currently set to {current_setting} which may reveal information about your server in a server signature")
                    print(f"Changing {current_setting} to Off will remove this signature")
                    print("Would you like to apply this change to make your server more secure? (Type 'no' to keep settings as they are, any other input will be interpreted as a 'yes')")
                    answer = input()
                    if answer not in ('no', 'No', 'NO'):
                        patched_conf.write("ServerSignature Off\n")
                        print("Setting was changed\n")
                    else:
                        patched_conf.write(line)
                        print("Setting was not changed\n")

            else:
                patched_conf.write(line)

main()