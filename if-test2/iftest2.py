#!/usr/bin/env python3.6
ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk == '192.168.0.1': # if any data is provided, this will test true
   print('Looks like the Gateway was set: ' + ipchk)
elif ipchk:
   print('Looks like the IP address was set: ' + ipchk) # indented under if
else: # if data is not provided
   print('You did not provide input.')

print('Exiting the program')
