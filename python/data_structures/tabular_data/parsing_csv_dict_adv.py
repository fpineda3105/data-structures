"""
CSV reader options.
"""

import csv
from csv_util import get_relative_path

def parse_to_dict(csvfilename, keyfield, separator, quote, quotestrategy):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a dictionary of dictionaries.
    """
    table = {}
    with open(csvfilename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile,
                                   skipinitialspace=True,
                                   delimiter=separator,
                                   quotechar=quote,
                                   quoting=quotestrategy)
        for row in csvreader:
            table[row[keyfield]] = row
    return table, csvreader.fieldnames


def print_table(table, fieldnames):
    """
    Print out table, which must be a dictionary
    of dictionaries, in a nicely formatted way.
    """
    print("{:<20}".format(fieldnames[0]), end='')
    for field in fieldnames[1:]:
        print("{:>6}".format(field), end='')
    print("")
    for name, row in table.items():
        # Header column left justified
        print("{:<19}".format(name), end='')
        # Remaining columns right justified
        for field in fieldnames[1:]:
            print("{:>6}".format(row[field]), end='')
        print("", end='\n')


firstFile = get_relative_path("csv","hightemp.csv")
table, fieldnames = parse_to_dict(firstFile, 'City', ',', '"', csv.QUOTE_MINIMAL)
print(fieldnames)
print_table(table, fieldnames)

print("")
print("")

secondFile = get_relative_path("csv","hightemp2.csv")
#csv.QUOTE_NONNUMERIC thats going to say that 
# every column that is not a number must be quoted
table2, fieldnames2 = parse_to_dict(secondFile, 'City', ',', '"', csv.QUOTE_NONNUMERIC)
print_table(table2, fieldnames2)

print("")
print("")

thirdFile = get_relative_path("csv","hightemp3.csv")
table3, fieldnames3 = parse_to_dict(thirdFile, 'City', ' ', "'", csv.QUOTE_NONNUMERIC)
print_table(table3, fieldnames3)