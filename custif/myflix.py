#!/usr/bin/env python3.6

message1 = 'The movie is about to begin, we recommend '
print('What is your connection speed in Mbps?')
connectspeed = float(input())
if connectspeed >= 25:
   message1 = message1 + 'setting video to 4k.'
elif connectspeed >= 5:
   message1 = message1 + 'setting video to 1080p.'
elif connectspeed >= 2:
   message1 = message1 + 'setting videeo to 720p.'
else:
   message1 = message1 + 'finding another access network.'

print(message1)
