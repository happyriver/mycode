#!/usr/bin/env python3.6
# Move file
import shutil
import os
os.chdir('/home/njiang/python/mycode')
shutil.move('raynor.obj', 'ceph_storage/')
# Rename file
xname = input('What is the new name for kerrign.obj?')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
