# Apache Blue

**BEST PRACTICES GUIDE AVAILABLE AT: https://apache-blue.gitbook.io/guide/**

Apache Blue is a guide to harden Apache web servers and make them more secure against outside attacks. It also includes a Python script that, when run against a server's .conf files, will update configuration settings to abide by best security practices. Apache Blue assumes working knowledge of Linux and a familiarity with the basics of how to use and install Apache. 

Best practices were based on the Center for Internet Security's Apache HTTP Server 2.4 Benchmark document, which can be found [here][1]. *While a lot of their recommendations have been tested for maximum efficacy, there is always the chance that they may not be right for you and your organization. **Due diligence is required before changing the configuration of any business critical systems.***

## How to read the guide

The guide is a comprehensive document that takes users through best practices for securing an Apache web server, outlining manual steps the user can make to implement each one. Whenever possible, the guide links to the corresponding Apache foundation documentation for the recommendation in question. Please note that while every configuration change the script makes is included in the guide, not all of the recommendations in the guide are automated by the script. Please read carefully when deciding which changes are appropriate for you and your organization.

This guide can be found [here][2].

## How to use the script

**REQUIREMENTS: The Apache Blue script uses the OS, colorama, and datetime modules for Python 3. Please make sure your Python libraries are up to date.**

The Python script, apache_blue.py, when run against the existing Apache .conf files, finds settings that are not in line with the recommendations mentioned in the guide, prompts the user for whether or not they want to change each setting, and then enacts that change if the user agrees. It also writes a log file that takes down the date and time these alterations were made, lists what settings were changed, and the files they were changed in for auditing purposes.

To use this script, in your terminal, enter 

`./apache_blue.py <full path to Apache root directory>`

and the script will walk through this directory and its subdirectories recursively to find configuration files and adjust settings as per user prompt. Typically, `/etc/apache2` is the default directory for Apache, but this may change depending on your environment and any customizations that may have been made. 

Each setting handled by the script references that setting's number in the guide and provides a link to it so the user can review if necessary. 

[1]: https://drive.google.com/file/d/1vCs7GY0hdpjl42u7_hpR5LzU9sfBIk-e/view
[2]: https://apache-blue.gitbook.io/guide/
