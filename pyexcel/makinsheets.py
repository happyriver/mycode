#!/usr/bin/env python3.6
# Export data to a spreadsheet file
#
# python -m pip3 install --user pyexcel
# python -m pip3 install --user pyexcel-xls
import pyexcel as pe

# Create a list of dictionary to export  (ROW1 = Vendor, ROW2 = Product)
mylistdict = [{'Vendor': 'Sun', 'Product': 'M5000'}, {'Vendor': 'HP', 'Product': 'HP3000'}, {'Vendor': 'IBM', 'Product': 'D1000'}]

# use the save_as function to create a xls file
pe.save_as(records=mylistdict, dest_file_name="server_list.xls")
