# Apache Blue

Apache Blue is a guide to harden Apache web servers and make them more secure against outside attacks. It also includes a Python script that, when run against a server's .conf files, will configure the server to abide by best practices for security. Patchy Apache assumes working knowledge of Linux, and a familiarity with how to use and install Apache, and is geared towards Apache users and administrators who want to make sure their server is as secure as possible. 

Best practices were based on the Center for Internet Security's Apache HTTP Server 2.4 Benchmark document, which can be found [here][1]. *While a lot of their recommendations have been tested for efficacy, there is always the chance that they may not be right for you and your organization. **Due diligence is required before changing the configuration of any business critical systems.***

## How to read the guide

The guide document takes users through best security practices for an Apache web server. These best practices are organized by category, and each one states a purpose to briefly explain what the setting does and why it makes sense to use the suggested setting, as well as why this affects security and why other settings can cause trouble. The default settings, if they exist, are also listed so the user can more easily find them. Whenever possible, the guide links to Apache foundation documentation for the setting in question.

This guide can be found [here][2].

## How to use the script

The included Python script, `apache_blue.py`, when run against the existing Apache `.conf` files, finds settings that are not in line with the best practices mentioned in the guide, prompts the user for whether or not they want to change each setting, and alters the file with the best practice setting if the user agrees. It also writes a log file that takes down the date and time these alterations were made, lists what settings were changed, and the files they were changed in for auditing purposes. 

To use this script, in your terminal, enter 

`./apache_blue.py <full path to Apache root directory>`

and the script will walk through this directory and its subdirectories recursively to find configuration files and adjust settings as per user prompt. Typically, `/etc/apache2` is the default directory for Apache, but this may change depending on your environment and any customizations that may have been made. 

Each setting handled by the script references that setting's number in the guide and provides a link to it so the user can review if necessary. 

[1]: https://drive.google.com/file/d/1vCs7GY0hdpjl42u7_hpR5LzU9sfBIk-e/view
[2]: https://apache-blue.gitbook.io/guide/
