import json

#JSON to direcotry
try:
    with open('sysmon-events.json') as f:
        data = json.loads(f.read())
        print(data)
except:
    print("No way")
try:
    tweets = []
    for line in open('sysmon-events.json.json', 'r'):
        tweets.append(json.loads(line))
except:
    print("No way")
counter=1 #variable for each line in JSON
#Looking for Enviromental Variable in SysmonLog

f=open('sysmon-events.json')
for x in f:
    if 'ParentCommand' in x:
        if 'HASHSESAD' in x:
            continue
        else:
            print(str(counter)+ x)
    counter+=1

'''
#Exception list
DllList=["msvcp90.dll","python27.dll","Cmsvcr90.dll","msvcm90.dll","python27.dll","msvcr90.dll"]
ExeList=["cmd.exe","powershell.exe","supply.exe","Sysmon.exe","chrome.exe","explorer.exe","mmc.exe","ftp.exe"
        ,"svchost.exe","consent.exe","mshta.exe","CompPkgSrv.exe"]
#Looking for first Command executed by malware

f=open('sysmon-events.json')
for x in f:
    if 'dll' in x:
        helper=0
        for i in range(len(DllList)):
            if DllList[i] in x:  #(str.__contains__('WELCOME', 'W'))
                helper=1
        if helper==0:
            print(str(counter) + " " + x)
    counter+=1
'''



