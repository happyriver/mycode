#!/usr/bin/env python3.6
# Export data to a spreadsheet file
#
# python -m pip3 install --user pyexcel
# python -m pip3 install --user pyexcel-xls
import pyexcel as pe
import os

# Create a list of dictionary to export  (ROW1 = Vendor, ROW2 = Product)
mylistdict = [{'Product': 'M300', 'Vendor': 'Sun'}, {'Product': 'HP3000', 'Vendor': 'HP'}, {'Product': 'D1000', 'Vendor': 'IBM'}]

# Get user input for the file dir
file_dir1 = input('Please enter the folder name: ')
for eachfile in os.listdir(file_dir1):
    print(eachfile)
# Get user input for the file name
file_name1 = input('Please type the file name you want, it can not be the same name as above: ')

# use the save_as function to create a xls file
pe.save_as(records=mylistdict, dest_file_name=file_name1)
