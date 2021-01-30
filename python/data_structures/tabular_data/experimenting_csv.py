"""
Examples code for experimenting with options to the csv.read() and csv.write() methods
"""
import csv
from csv_util import get_relative_path


# Function that prints 2D table to console

def print_table(table):
    """
    Echo a nested list to the console
    """
    for row in table:
        print(row)


# Options for reading a CSV file

def read_csv_file(file_name: str, file_delimeter: str) -> list:
    """
    Given a CSV file path and a delimiter as strings,
    read the data into a 2D table and return the table
    """

    # don't need to explicitly close the file now
    with open(file_name, newline='') as csv_file:
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=file_delimeter)
        for row in csv_reader:
            csv_table.append(row)
    return csv_table


def csv_delimiter_examples() -> None:
    """
    Run some example of reading CSV files using different delimiter options
    """
    number_file = get_relative_path('csv', 'number_table.csv')
    number_table = read_csv_file(number_file, " ")
    print_table(number_table)

    print()

    name_file = get_relative_path('csv', 'name_table.csv')
    name_table = read_csv_file(name_file, ",")
    print_table(name_table)


csv_delimiter_examples()


# Options for writing a CSV file

def write_csv_file(csv_table: list, file_name: str, file_delimiter: str, quoting_value: str) -> None:
    """
    Given a nested list csv_table, write the data into a
    CSV file with the name file_name
    """

    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=file_delimiter, quoting=quoting_value)
        for row in csv_table:
            csv_writer.writerow(row)


def csv_quoting_examples():
    """
    Run some example of writing 2D tables as CSV files using various quoting options
    """
    name_file = get_relative_path("csv", "name_table.csv")
    name_table = read_csv_file(name_file, ",")
    name_table.append([1, 2, 3])
    write_csv_file(name_table, get_relative_path(
        "csv", "name_table_minimal.csv"), ",", csv.QUOTE_MINIMAL)
    write_csv_file(name_table, get_relative_path(
        "csv", "name_table_all.csv"), ",", csv.QUOTE_ALL)
    write_csv_file(name_table, get_relative_path(
        "csv", "name_table_nonnumeric.csv"), ",", csv.QUOTE_NONNUMERIC)
    # write_csv_file(name_table, "name_table_none.csv", ",", csv.QUOTE_NONE)        # no escapechar is set for lots of quotes


csv_quoting_examples()
