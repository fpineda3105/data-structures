"""
Example code to read and parse a CSV file.
"""

import os

def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    with open(csvfilename, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(',')
            table.append(columns)
    return table


def print_table(table):
    """
    Print out table, which must be a list
    of lists, in a nicely formatted way.
    """
    for row in table:
        # Header column left justified
        print("{:<19}".format(row[0]), end='')
        # Remaining columns right justified
        for col in row[1:]:
            print("{:>4}".format(col), end='')
        print("", end='\n')

import os
working_dir = os.getcwd()

def get_relative_path(folder,csvfilename):
    return os.path.join(working_dir,folder,csvfilename)

firstFile = get_relative_path("csv","hightemp.csv")
table = parse(firstFile)
print_table(table)

print("")
print("")

secondFile = get_relative_path("csv","hightemp2.csv")
table2 = parse(secondFile)
print_table(table2)
