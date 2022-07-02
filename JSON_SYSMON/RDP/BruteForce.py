#RDP Bruteforce
import re
data = []
counter = 0
portRange = []
try:
    f = open('BTLO_Bruteforce_Challenge.txt')
    for x in f:
        #counting Aduit Failure
        '''
        if 'Audit Failure' in x:
            counter+=1
            print(counter)
        '''
        #display all targeted user name
        '''
        if 'Account Name:' in x :
            print(x)
        '''
        #failure reason
        '''
        if 'Failure Reason:' in x:
            print(x)
        '''
        #header of log / Audit Success
        '''
        if 'Audit Failure' in x:
            print(x)
        '''
        # sourceIp
        '''
        if 'Source Network Address:' in x:
            print(x)
        '''
        #sourcePort - Range with sort 
        if 'Source Port:' in x:
            portRange.append(x)
    portRange.sort()
    for x in portRange:
        print(x)

        
except:
    print("No way")
