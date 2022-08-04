#Looking for IP Address
# importing the module
import re
f=open('access.log')
linecounter=0

# Identiti URI admin access with TOKEN
lst=[]
'''
for x in f:
    if  'adminlogin' in x:
       if 'POST' in x:
        if '.php?' in x:
            lst.append(x[45:])
        else:
            #print(str(linecounter)+ " " + x)
            continue
    linecounter+=1
'''
#Looking for wordpress hacktool
'''
for x in f:
    if  '.org' in x:
            lst.append(x[45:])
'''
# PHP WEBSHELL
#119.241.22.121 168.22.54.119
'''
for x in f: #302 correct login
    if  '.php' in x:
        if 'wp-login.php' in x:
            continue
        else:
            lst.append(x[:])

#103.69.55.212 - - [14/Jan/2021:06:30:05 +0000] "GET /wp-content/uploads/simple-file-list/fr34k.php HTTP/1.1" 404 488 "-" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0)"

lst = list(dict.fromkeys(lst))
for x in lst:
    print(x)
    a=32
'''
#looking for plugin exploited -> access
for x in f: #302 correct login
    if  'simple-file-list' in x:
        if'ver'in x:
            lst.append(x[:])

#103.69.55.212 - - [14/Jan/2021:06:30:05 +0000] "GET /wp-content/uploads/simple-file-list/fr34k.php HTTP/1.1" 404 488 "-" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0)"

lst = list(dict.fromkeys(lst))
for x in lst:
    print(x)
    a=32
