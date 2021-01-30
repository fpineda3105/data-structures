from  project_csv import read_csv_fieldnames
from csv_util import get_relative_path


def test_read_csv_to_list():
    expected = [['Field1', 'Field2', 'Field3', 'Field4'],
              ['1', '2', '3', '4'],['5', '6', '7', '8'],['9', '10', '11', '12']]
    
    filename = get_relative_path('project_data','table1.csv')
    separator = ','
    quote = "'"
    
    assert expected == read_csv_fieldnames(filename, separator, quote)
    
    
