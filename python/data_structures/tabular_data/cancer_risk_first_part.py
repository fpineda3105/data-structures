"""
Week 3 practice project template for Python Data Analysis
Reading and writing CSV files using lists
"""

from csv_util import get_relative_path
import csv


#########################################################
# Part 1 - Week 3

def print_table(table):
    """
    Echo a nested listto the console
    """
    for row in table:
        print(row)


def read_csv_file(file_name: str) -> list:
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """

    with open(file_name, 'r', newline='') as csvfile:
        csv_table = []
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            csv_table.append(row)

    return csv_table


def write_csv_file(csv_table: str, file_name: str) -> None:
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        for row in csv_table:
            csv_writer.writerow(row)


def test_part1_code() -> None:
    """
    Run examples that test the functions for part 1
    """

    # Simple test for reader
    test_file = get_relative_path("cancer_data", "test_case.csv")
    test_table = read_csv_file(test_file)  # create a small CSV for this test
    print_table(test_table)
    print()

    # Test the writer
    cancer_risk_table = read_csv_file(get_relative_path(
        "cancer_data", "cancer_risk05_v4_county.csv"))

    cancer_data_copy_file = get_relative_path(
        "cancer_data", "cancer_risk05_v4_county_copy.csv")
    write_csv_file(cancer_risk_table, cancer_data_copy_file)
    cancer_risk_copy = read_csv_file(cancer_data_copy_file)

    # Test whether two tables are the same
    assert cancer_risk_table == cancer_risk_copy


test_part1_code()
