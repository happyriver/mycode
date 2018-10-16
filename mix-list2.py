#!/usr/bin/env python3.6
# Append list
proto = ['ssh', 'http', 'https']
print(proto)
print(proto[1])
proto.extend('dns') # this line will add 'dns' to the end of the list
print(proto)
proto.append('udp') # pass 
print(proto)
proto2 = [2, 3, 4]
proto.extend(proto2)
print(proto)
proto.append(proto2) # pass proto2 as an argumeent to the append method
print(proto)
