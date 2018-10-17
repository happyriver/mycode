#!/usr/bin/env python3.6
# Read sheet file
import os
import pyexcel
# "example.csv", "example.xlsx", "exadmple.ods", "example.xlsm"
base_dir = os.getcwd()
spreadsheet = pyexcel.get_sheet(file_name=os.path.join(base_dir, "example.xls"))

# rows() returns row based iterator, meaning it can be iterated row by row
for row in spreadsheet:
    print(row)

# Alternatively, you can use::
#   for row in spreadsheet:
#       print row
# becasue by default **Reader** regards itself a row based iterator.

print("Read data column based.")
for value in spreadsheet.columns():
    print(value)
