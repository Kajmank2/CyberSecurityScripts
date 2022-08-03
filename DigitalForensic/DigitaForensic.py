#Looking for IP Address
# importing the module
import re
f=open('sshlog.log')
linecounter=0
'''
# opening and reading the file
with open('sshlog.log') as fh:
    fstring = fh.readlines()

# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# initializing the list object
lst = []

# extracting the IP addresses
for line in fstring:
   x= pattern.search(line)
   if x == None:
       continue
   else:
       lst.append(x[0])
# displaying the extracted IP addresses
print(lst)
'''
###SUCESSFULL LOGIN ###
#STRING
'Accepted password'

#log file located

lst=[]
for x in f:
    if  'C:/' in x:
        if 'OpenSSH-Win64' in x:
            continue
        else:
            #print(str(linecounter)+ " " + x)
            lst.append(x)
    linecounter+=1
lst = list(dict.fromkeys(lst))
for x in lst:
    print(x)
    a=32
'''
#When was the first request from the attacker recorded? (5 points)

lst=[]
for x in f:
    if  'Connection' in x:
        if 'xzdsadsa' in x:
            continue
        else:
            #print(str(linecounter)+ " " + x)
            lst.append(x)
    linecounter+=1
lst = list(dict.fromkeys(lst))
for x in lst:
    print(x)
    a=32
'''
#Looking for invalid user
'''
for x in f:
    if 'Invalid user' in x:
        print(x)
'''
# GCC
# Looking for valid account
'''
lst=[]
for x in f:
    if 'Failed password ' in x:
        if 'invalid' in x:
            continue
        else:
            #print(str(linecounter)+ " " + x)
            lst.append(x[29:])
    linecounter+=1
lst = list(dict.fromkeys(lst))
for x in lst:
    print(x)
    a=32
# delete duplicate
'''
'''
listwihtouduplicate=[]
for x in f:
    listwihtouduplicate.append(x[29:])
listwihtouduplicate = list(dict.fromkeys(listwihtouduplicate))
for x in listwihtouduplicate:
    print(x)
    a=32
'''
#Exception list
DllList=["msvcp90.dll","python27.dll","Cmsvcr90.dll","msvcm90.dll","python27.dll","msvcr90.dll"]
ExeList=["cmd.exe","powershell.exe","supply.exe","Sysmon.exe","chrome.exe","explorer.exe","mmc.exe","ftp.exe"
        ,"svchost.exe","consent.exe","mshta.exe","CompPkgSrv.exe"]
ExcptionList=["invalid",'unable to generate','unable','failed','failure','does not exist','not authenticated','Invalid',' user specific delay 0.000ms','try method password'
              'userauth-request']

#Looking all valideted users in our data
'''
counter =0
lst=[]
for x in f:
    if 'userauth-request for user' in x:
     if 'ssh-connection method none' in x :
        helper = 0
        for i in range(len(ExcptionList)):
            if ExcptionList[i] in x:  #(str.__contains__('WELCOME', 'W'))
                helper=1
        if helper == 0:
            print(str(counter) + " " + x[35:])
            #lst.append(x[34:])
    counter += 1
#delete duplicate
lst = list(dict.fromkeys(lst))
for x in lst:
    print(x)
    a=32
'''

