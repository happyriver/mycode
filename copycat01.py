#!/usr/bin/env python3.6

# Copy file
# shutil: shell utility
import shutil
import os
os.chdir('/home/njiang/python/mycode/')
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
shutil.copytree('5g_research/', '5g_research_backup/')
