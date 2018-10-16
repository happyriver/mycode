#!/usr/bin/env python3.6
x = 0
menulist1 = ['Access issue', 'NFS file system issue', 'Account issue']
for i in menulist1:
  print(str(x) + ': ' + i)
  x += 1

userproblem = input('What issue are you having, please enter the number: ')
if int(userproblem) == 0:
   print('You have ' +  menulist1[0])
   ipaddress1 = input('What IP address is which you failed to access: ')
   username1 = input('What is the user name used: ')
   print('Problem: ' + username1 + ' is not able to access ' + ipaddress1)
elif int(userproblem) == 1:
   print('You have ' +  menulist1[1])
   nfsfile1 = input('What the nfs file system has issue with: ')
   hostname1 = input('What is the hostname the nfs file system resides: ')
   print('The nfs file system ' + nfsfile1 + ' on ' + hostname1 + ' is not working.')
else:
   print('You have ' +  menulist1[2])
   username1 = input('What is the user name used: ')
   hostname1 = input('What is the hostname the user ' + username1 + ' is not working: ')
   print('The user account ' + username1 + ' on ' + hostname1 + ' has problem.')


quitans = input('Do you want to exit the program?(y/n) ')
if quitans.lower() == 'y':
   print('Exiting program.')
   exit
else:
   print('User does not want to quit, but no way now.')
   exit

