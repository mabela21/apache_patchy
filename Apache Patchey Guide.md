# Apache Patchey Guide


# Preventing Information Leakage

The more details that are readily available to the public about your Apache setup, the greater the chances that Apache itself will be used as an attack vector, allowing malicious actors access to your network. The following changes are designed to help hide details about your apache setup from prying eyes.

**[1] Confirm that the Apache *ServerTokens* directive exists in the configuration file, and set the value to *Prod* or *ProductOnly***
    - PURPOSE: This will prevent Apache version or module information from appearing in the server HTTP response header. Instead, only the name of the product - Apache - will appear. 
    - In most cases, the default value of this directive will be set to Full.

**[2] Confirm that the *ServerSignature* directive exists in the configuration file, and set the value to *Off***
    - PURPOSE: This will prevent Apache version and OS information from appearing in the footer of error and other pages. Instead, nothing will appear.
    - In most cases, the default value is already set to Off, but it is important to take the extra time to *ensure* it.
    
    *reinsert* [3]
    
**[4] Confirm that the *FileETag* directive either does not exist in the configuration file, or that it is set to *None* or *MTime Size***
    - PURPOSE: This will prevent file inode numbers from being included in returned values of the Etag response header fields. Inode information is senstive and can be useful in development of exploits to gain a foothold in your sytem.
    - In most cases the default value is set to MTime size, but it is important to take the extra time to *ensure* it
    
# Mitigating Denial of Service Attacks

Denial of Service (DoS) attacks are designed to overload and possibly bring down a system or a network, preventing it from being able to functon normally. Usually the attackers flood the server with excessive requests, forcing it to use critical resources and preventing it from being able to attend to or handle legitimate client traffic. The following changes are designed to increase the server's resiliency to these attacks by adjusting how long connections are maintained and allowing single socket connections to efficiently handle more requests.

**[1] Confirm that the *Timeout* directive exists in the configuration file, and set the value to *10* or lower**
    - PURPOSE: This will lower the number of active connections to the server at any given time by letting go of older connections sooner. PLEASE NOTE that the Apache Timeout directive controls more than one timeout value, you should carefully review the Foundation's own documentation so you'll have a clear view of the scope of any changes you make. http://httpd.apache.org/docs/2.4/mod/core.html#timeout
    - In most cases, the default value is set to 60 seconds
    
**[2] Confirm that the *KeepAlive* directive exists in the configuration file, and set the value to *On***
    - PURPOSE: This will lower the number of active connections by reusing a single client's TCP socket connection client to process subsequent HTTP requests from that client. 
    - In most cases, the default value is set to On but it is important to take the extra time to *ensure* it

**[3] Confirm that the *MaxKeepAliveRequests* directive exists in the configuration file, and set the value to *100* or more**
    - PURPOSE: This will reduce the pull on resources required to setup and sever new TCP connections for every request. More requests from a single client can now be sent using the same TCP connection
    - In most cases, the default value is set to 100 but it is important to take the extra time to *ensure* it

**[4] Confirm that the *KeepAliveTimeout* directive exists in the configuration file, and set the value to *15* or less**
    - PURPOSE: This will prevent old *unused* TCP connections from lasting longer than 15 seconds, increasing efficiency.
    - In most cases, the default value is set to 5

**[5] Confirm that the mod_requesttimeout module is being loaded in the configuration file as so: "LoadModule reqtimeout_module modules/mod_reqtimeout.so" and that the RequestReadTimeout directive exists. Set the *header* value to *40* or less, and the corresponding *MinRate* to *500***
    - PURPOSE: This will mitigate potential DoS attacks by placing a timeout limit for the header portion of client requests. The directive's header values include an initial timeout value, a maximum timeout, and a minimum rate (after the initial timeout, the minimum rate indicates how many bytes the server will wait an additional 1 second for -> 1 sec/N bytes received). Slow requests are common in DoS attacks and a significant drain of resources.
    - In most cases, the default values are set as follows: header=20-40, MinRate=500 but it is important to take the extra time to *ensure* it

**[6] Confirm that the mod_requesttimeout module is being loaded in the configuration file as so: "LoadModule reqtimeout_module modules/mod_reqtimeout.so" and that the RequestReadTimeout directive exists. Set the *body* value to *20*, and the corresponding *MinRate* to *500***
    - PURPOSE: This will mitigate potential DoS attacks by placing a timeout limit for the body portion of client requests. The directive's body values include an initial timeout value, a maximum timeout, and a minimum rate (after the initial timeout, the minimum rate indicates how many bytes the server will wait an additional 1 second for -> 1 sec/N bytes received). Slow requests are common in DoS attacks and a significant drain of resources.
    - In most cases, the default values are set as follows: body=20, MinRate=500 but it is important to take the extra time to *ensure* it

