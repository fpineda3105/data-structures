"""
Using csv.DictReader.
"""

import csv
from csv_util import get_relative_path

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr',
          'May', 'Jun', 'Jul', 'Aug',
          'Sep', 'Oct', 'Nov', 'Dec')

def parse_to_dict(csvfilename, keyfield):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a dictionary of dictionaries.
    """
    table = {}
    with open(csvfilename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   skipinitialspace=True)        
        for row in csvreader:
            table[row[keyfield]] = row
    return table


def print_table(table):
    """
    Print out table, which must be a dictionary
    of dictionaries, in a nicely formatted way.
    """
    print("City               ", end='')
    for month in MONTHS:
        print("{:>6}".format(month), end='')
    print("")
    for name, row in table.items():
        # Header column left justified
        print("{:<19}".format(name), end='')
        # Remaining columns right justified
        for month in MONTHS:
            print("{:>6}".format(row[month]), end='')
        print("", end='\n')



firstFile = get_relative_path("csv","hightemp.csv")
table = parse_to_dict(firstFile, 'City')
print_table(table)


