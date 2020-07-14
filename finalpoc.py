#!/usr/bin/env python3

import os

def main():

    original_conf_contents = []

    ServerTokens_isPresent = False
    ServerSignature_isPresent = False
    FileETag_isPresent = False
    Timeout_isPresent = False
    KeepAlive_isPresent = False
    MaxKeepAliveRequests_isPresent = False
    KeepAliveTimeout_isPresent = False

    with open("ch8.conf", "r") as original_conf:
        original_conf_contents = original_conf.readlines()

    os.rename("ch8.conf", "ch8.conf.bak")

    with open("ch8.conf", "w+") as patched_conf, open("apatchy.log", "a+") as ap_log:

        for line in original_conf_contents:

            if "ServerTokens" in line:
                ServerTokens_isPresent = True
                if "Prod" not in line:
                    current_setting = line.replace("ServerTokens ", '').strip()
                    print(f"ServerTokens is currently set to {current_setting} which could potentially reveal Apache version and module information to hackers, allowing them to find exploits")
                    print(f"Changing {current_setting} to Prod will only display 'Apache' and will not show any version numbers")
                    print("Would you like to apply this change to make your server more secure? [Y/n]")
                    answer = input()
                    while answer not in ('Y', 'y', 'N', 'n'):
                        print("Invalid response, need 'y' or 'n'")
                        answer = input()
                    if answer in ('Y', 'y'):
                        patched_conf.write("ServerTokens Prod\n")
                        print("Setting was changed\n")
                        ap_log.write("User opted to set ServerTokens to 'Prod'\n")
                    elif answer in ('N', 'n'):
                        patched_conf.write(line)
                        print("Setting was not changed\n")
                        ap_log.write("User opted NOT to set ServerTokens to 'Prod'\n")
                else:
                    patched_conf.write(line)
            
            elif "ServerSignature" in line:
                ServerSignature_isPresent = True
                if "Off" not in line:
                    current_setting = line.replace("ServerSignature ", '').strip()
                    print(f"ServerSignature is currently set to {current_setting} which may reveal information about your server in a server signature")
                    print(f"Changing {current_setting} to Off will remove this signature")
                    print("Would you like to apply this change to make your server more secure? [Y/n]")
                    answer = input()
                    while answer not in ('Y', 'y', 'N', 'n'):
                        print("Invalid response, need 'y' or 'n'")
                        answer = input()
                    if answer in ('Y', 'y'):
                        patched_conf.write("ServerSignature Off\n")
                        print("Setting was changed\n")
                        ap_log.write("User opted to set ServerSignature to 'Off'\n")
                    elif answer in ('N', 'n'):
                        patched_conf.write(line)
                        print("Setting was not changed\n")
                        ap_log.write("User opted NOT to set ServerSignature to 'Off'\n")
                else:
                    patched_conf.write(line)

            elif "FileETag" in line:
                FileETag_isPresent = True
                current_setting = line.replace("FileETag ", '').strip()
                if current_setting not in ("None", "MTime Size"):
                    print(f"FileETag is currently set to {current_setting}, best practice says it should be set to None or MTime Size")
                    print("Would you like to change this setting? [Y/n]")
                    answer = input()
                    while answer not in ('Y', 'y', 'N', 'n'):
                        print("Invalid response, need 'y' or 'n'")
                        answer = input()
                    if answer in ('Y', 'y'):
                        print("If you would like to change this setting to MTime Size, type 'm', otherwise None will be set")
                        answer = input()
                        if answer in ('M', 'm'):
                            patched_conf.write("FileETag MTime Size\n")
                            print("Setting was changed\n")
                            ap_log.write("User opted to set FileETag to 'MTime Size'\n")
                        else:
                            patched_conf.write("FileETag None\n")
                            print("Setting was changed\n")
                            ap_log.write("User opted to set FileETag to 'None'\n")
                    elif answer in ('N', 'n'):
                        patched_conf.write(line)
                        print("Setting was not changed\n")
                        ap_log.write("User opted NOT to change FileETag value\n")
                else:
                    patched_conf.write(line)
            
            elif "Timeout" in line and "Keep" not in line:
                Timeout_isPresent = True 
                current_setting = int(line.replace("Timeout ", ''))
                if current_setting > 10:
                    print(f"Timeout is currently set to {current_setting}, best practice says it should be 10 or less")
                    print("Would you like to change this setting to 10? [Y/n]")
                    answer = input()
                    while answer not in ('Y', 'y', 'N', 'n'):
                        print("Invalid response, need 'y' or 'n'")
                        answer = input()
                    if answer in ('Y', 'y'):
                        patched_conf.write("Timeout 10\n")
                        print("Setting was changed\n")
                        ap_log.write("User opted to set Timeout to 10\n")
                    elif answer in ('N', 'n'):
                        patched_conf.write(line)
                        print("Setting was not changed\n")
                        ap_log.write("User opted NOT to set Timeout to 10\n")
                else:
                    patched_conf.write(line)

            elif "KeepAlive " in line:
                KeepAlive_isPresent = True 
                current_setting = line.replace("KeepAlive ", '').strip()
                if current_setting != "On":
                    print(f"KeepAlive is currently set to {current_setting}, best practice says it should be set to On")
                    print("Would you like to change this setting to On? [Y/n]")
                    answer = input()
                    while answer not in ('Y', 'y', 'N', 'n'):
                        print("Invalid response, need 'y' or 'n'")
                        answer = input()
                    if answer in ('Y', 'y'):
                        patched_conf.write("KeepAlive On\n")
                        print("Setting was changed\n")
                        ap_log.write("User opted to set KeepAlive to 'On'\n")
                    elif answer in ('N', 'n'):
                        patched_conf.write(line)
                        print("Setting was not changed\n")
                        ap_log.write("User opted NOT to set KeepAlive to 'On'\n")
                else:
                    patched_conf.write(line)

            elif "MaxKeepAliveRequests" in line:
                MaxKeepAliveRequests_isPresent = True 
                current_setting = int(line.replace("MaxKeepAliveRequests ", ''))
                if current_setting < 100:
                    print(f"MaxKeepAliveRequests is currently set to {current_setting}, best practice says it should be 100 or more")
                    print("Would you like to change this setting to 100? [Y/n]")
                    answer = input()
                    while answer not in ('Y', 'y', 'N', 'n'):
                        print("Invalid response, need 'y' or 'n'")
                        answer = input()
                    if answer in ('Y', 'y'):
                        patched_conf.write("MaxKeepAliveRequests 100\n")
                        print("Setting was changed\n")
                        ap_log.write("User opted to set MaxKeepAliveRequests to 100\n")
                    elif answer in ('N', 'n'):
                        patched_conf.write(line)
                        print("Setting was not changed\n")
                        ap_log.write("User opted NOT to set MaxKeepAliveRequests to 100\n")
                else:
                    patched_conf.write(line)
            
            elif "KeepAliveTimeout" in line:
                KeepAliveTimeout_isPresent = True 
                current_setting = int(line.replace("KeepAliveTimeout ", ''))
                if current_setting < 15:
                    print(f"Timeout is currently set to {current_setting}, best practice says it should be 15 or more")
                    print("Would you like to change this setting to 15? [Y/n]")
                    answer = input()
                    while answer not in ('Y', 'y', 'N', 'n'):
                        print("Invalid response, need 'y' or 'n'")
                        answer = input()
                    if answer in ('Y', 'y'):
                        patched_conf.write("KeepAliveTimeout 15\n")
                        print("Setting was changed\n")
                        ap_log.write("User opted to set KeepAliveTimeout to 15\n")
                    elif answer in ('N', 'n'):
                        patched_conf.write(line)
                        print("Setting was not changed\n")
                        ap_log.write("User opted NOT to set KeepAliveTimeout to 15\n")
                else:
                    patched_conf.write(line)
            
            else:
                patched_conf.write(line)
        
        if not ServerTokens_isPresent:
            print("A ServerTokens directive is not present, best practice dictates it should be set to Prod, would you like to add it? [Y/n]")
            answer = input()
            while answer not in ('Y', 'y', 'N', 'n'):
                print("Invalid response, need 'y' or 'n'")
                answer = input()
            if answer in ('Y', 'y'):
                patched_conf.write("\nServerTokens Prod")
                print("Setting added to file\n")
                ap_log.write("User opted to create the ServerTokens directive and set the value to 'Prod'\n")
            elif answer in ('N', 'n'):
                print("Skipped adding setting to file\n")
                ap_log.write("User opted NOT to create the ServerTokens directive\n")
        
        if not ServerSignature_isPresent:
            print("A ServerSignature directive is not present, best practice dictates it should be set to Off, would you like to add it? [Y/n]")
            answer = input()
            while answer not in ('Y', 'y', 'N', 'n'):
                print("Invalid response, need 'y' or 'n'")
                answer = input()
            if answer in ('Y', 'y'):
                patched_conf.write("\nServerSignature Off")
                print("Setting added to file\n")
                ap_log.write("User opted to create the ServerSignature directive and set the value to 'Off'\n")
            elif answer in ('N', 'n'):
                print("Skipped adding setting to file\n")
                ap_log.write("User opted NOT to create the ServerSignature directive\n")

        if not FileETag_isPresent:
            print("A FileETag directive is not present, would you like to add it? [Y/n]")
            answer = input()
            while answer not in ('Y', 'y', 'N', 'n'):
                print("Invalid response, need 'y' or 'n'")
                answer = input()
            if answer in ('Y', 'y'):
                print("Best practice dictates this directive be set to None or MTime Size, type 'm' to set to MTime Size, anything else will set to None")
                answer = input()
                if answer in ('M', 'm'):
                    patched_conf.write("\nFileETag MTime Size")
                    print("Setting was added to file\n")
                    ap_log.write("User opted to create the FileETag directive and set the value to 'MTime Size'\n")
                else:
                    patched_conf.write("\nFileETag None")
                    print("Setting was added to file\n")
                    ap_log.write("User opted to create the FileETag directive and set the value to 'None'\n")
            elif answer in ('N', 'n'):
                print("Skipped adding setting to file\n")
                ap_log.write("User opted NOT to create the FileETag directive\n")

        if not Timeout_isPresent:
            print("A Timeout directive is not present, best practice dictates it should be set to 10 or less, would you like to add it? [Y/n]")
            answer = input()
            while answer not in ('Y', 'y', 'N', 'n'):
                print("Invalid response, need 'y' or 'n'")
                answer = input()
            if answer in ('Y', 'y'):
                patched_conf.write("\nTimeout 10")
                print("Setting added to file\n")
                ap_log.write("User opted to create the Timeout directive and set the value to 10\n")
            elif answer in ('N', 'n'):
                print("Skipped adding setting to file\n")
                ap_log.write("User opted NOT to create the Timeout directive and set the value to 10\n")
        
        if not KeepAlive_isPresent:
            print("A KeepAlive directive is not present, best practice dictates it should be set to On, would you like to add it? [Y/n]")
            answer = input()
            while answer not in ('Y', 'y', 'N', 'n'):
                print("Invalid response, need 'y' or 'n'")
                answer = input()
            if answer in ('Y', 'y'):
                patched_conf.write("\nKeepAlive On")
                print("Setting added to file\n")
                ap_log.write("User opted to create the KeepAlive directive and set the value to 'On'\n")
            elif answer in ('N', 'n'):
                print("Skipped adding setting to file\n")
                ap_log.write("User opted to create the KeepAlive directive and set the value to 'On'\n")

        if not MaxKeepAliveRequests_isPresent:
            print("A MaxKeepAliveRequests directive is not present, best practice dictates it should be set to 100 or more, would you like to add it? [Y/n]")
            answer = input()
            while answer not in ('Y', 'y', 'N', 'n'):
                print("Invalid response, need 'y' or 'n'")
                answer = input()
            if answer in ('Y', 'y'):
                patched_conf.write("\nMaxKeepAliveRequests 100")
                print("Setting added to file\n")
                ap_log.write("User opted to create the MaxKeepAliveRequests directive and set the value to 100\n")
            elif answer in ('N', 'n'):
                print("Skipped adding setting to file\n")
                ap_log.write("User opted NOT to create the MaxKeepAliveRequests directive and set the value to 100\n")

        if not KeepAliveTimeout_isPresent:
            print("A KeepAliveTimeout directive is not present, best practice dictates it should be set to 15 or more, would you like to add it? [Y/n]")
            answer = input()
            while answer not in ('Y', 'y', 'N', 'n'):
                print("Invalid response, need 'y' or 'n'")
                answer = input()
            if answer in ('Y', 'y'):
                patched_conf.write("\nKeepAliveTimeout 15")
                print("Setting added to file\n")
                ap_log.write("User opted to create the KeepAliveTimeout directive and set the value to 15\n")
            elif answer in ('N', 'n'):
                print("Skipped adding setting to file\n")
                ap_log.write("User opted NOT to create the KeepAliveTimeout directive and set the value to 15\n")
    
    print("All done! To review the changes you made, please visit the 'apatchy.log' file")

main()