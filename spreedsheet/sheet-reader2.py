#!/usr/bin/env python3.6
# Read sheet file
import os
import pyexcel as pe
# "example.csv", "example.xlsx", "exadmple.ods", "example.xlsm"
base_dir = os.getcwd()
spreadsheet = pe.get_sheet(file_name=os.path.join(base_dir, "example.xls"))

# row_range() gives [0 .. number of rows]
for r in spreadsheet.row_range():
# column_range() gives [0 .. number of ranges]
    for c in spreadsheet.column_range():
# cell_value(row_index, colum_index), row_index and colum_index starts from 0
        print(spreadsheet.cell_value(r,c))
