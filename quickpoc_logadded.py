#!/usr/bin/env python3

import os

def main():

    original_conf_contents = []

    ServerTokens_isPresent = False
    ServerSignature_isPresent = False
    FileETags_isPresent = False

    with open("ch8.conf", "r") as original_conf:
        original_conf_contents = original_conf.readlines()

    os.rename("ch8.conf", "ch8.conf.bak")

    with open("ch8.conf", "w+") as patched_conf, open ("apatchy.log", "a+") as ap_log:
        for line in original_conf_contents:

            if "ServerTokens" in line:
                ServerTokens_isPresent = True
                if "Prod" not in line:
                    current_setting = line.replace("ServerTokens ", '').strip()
                    print(f"ServerTokens is currently set to {current_setting} which could potentially reveal Apache version and module information to hackers, allowing them to find exploits")
                    print(f"Changing {current_setting} to Prod will only display 'Apache' and will not show any version numbers")
                    print("Would you like to apply this change to make your server more secure? [Y/n]")
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
                        print("Invalid response. C'mon dude.")
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
                    if answer in ('Y', 'y'):
                        patched_conf.write("ServerSignature Off\n")
                        print("Setting was changed\n")
                        ap_log.write("User opted to set ServerSignature to 'Off'\n")
                    elif answer in ('N', 'n'):
                        patched_conf.write(line)
                        print("Setting was not changed\n")
                        ap_log.write("User opted NOT to set ServerSignature to 'Off'\n")
                    else:
                        print("Invalid response. C'mon dude.")
                else:
                    patched_conf.write(line)

            elif "FileETag" in line:
                FileETags_isPresent = True
                current_setting = line.replace("FileETag ", '')
                if current_setting not in ("None", "MTime Size"):
                    print(f"FileETag is currently set to {current_setting}, best practice says it should be set to None or MTime Size")
                    print("Would you like to change this setting? [Y/n]")
                    answer = input()
                    if answer in ('Y', 'y'):
                        print("If you would like to change this setting to MTime Size, type 'm', otherwise None will be set")
                        answer = input()
                        if answer in ('M', 'm'):
                            patched_conf.write("FileETag MTime Size")
                            print("Setting was changed\n")
                            ap_log.write("User opted to set FileETag to 'MTime Size'\n")
                        else:
                            patched_conf.write("FileETag None")
                            print("Setting was changed\n")
                            ap_log.write("User opted to set FileETag to 'None'\n")
                    elif answer in ('N', 'n'):
                        patched_conf.write(line)
                        print("Setting was not changed\n")
                        ap_log.write("User opted NOT to change FileETag value\n")
                    else:
                        print("Invalid response. C'mon dude.")
                else:
                    patched_conf.write(line)

            else:
                patched_conf.write(line)
        
        if not ServerTokens_isPresent:
            print("A ServerTokens directive is not present, best practice dictates it should be set to Prod, would you like to add it? [Y/n]")
            answer = input()
            if answer in ('Y', 'y'):
                patched_conf.write("\nServerTokens Prod")
                print("Setting added to file\n")
                ap_log.write("User opted to create the ServerTokens directive and set the value to 'Prod'\n")
            elif answer in ('N', 'n'):
                print("Skipped adding setting to file\n")
                ap_log.write("User opted NOT to create the ServerTokens directive\n")
            else:
                print("Invalid response. C'mon dude.")
        
        if not ServerSignature_isPresent:
            print("A ServerSignature directive is not present, best practice dictates it should be set to Off, would you like to add it? [Y/n]")
            answer = input()
            if answer in ('Y', 'y'):
                patched_conf.write("\nServerSignature Off")
                print("Setting added to file\n")
                ap_log.write("User opted to create the ServerSignature directive and set the value to 'Off'\n")
            elif answer in ('N', 'n'):
                print("Skipped adding setting to file\n")
                ap_log.write("User opted NOT to create the ServerSignature directive\n")
            else:
                print("Invalid response. C'mon dude.")

        if not FileETags_isPresent:
            print("A FileETags directive is not present, would you like to add it? [Y/n]")
            answer = input()
            if answer in ('Y', 'y'):
                print("Best practice dictates this directive be set to None or MTime Size, type 'm' to set to MTime Size, anything else will set to None")
                answer = input()
                if answer in ('M', 'm'):
                    patched_conf.write("\nFileETag MTime Size")
                    print("Setting was added to file\n")
                    ap_log.write("User opted to create the FileETag directive and set the value to 'MTime Size'\n")
                else:
                    patched_conf.write("\nFIleETag None")
                    print("Setting was added to file\n")
                    ap_log.write("User opted to create the FileETag directive and set the value to 'None'\n")
            elif answer in ('N', 'n'):
                print("Skipped adding setting to file\n")
                ap_log.write("User opted NOT to create the FileETag directive\n")
            else:
                print("Invalid response. C'mon dude.")
                
            

    print("All done! To review the changes you made, please visit the 'apatchy.log' file")

main()