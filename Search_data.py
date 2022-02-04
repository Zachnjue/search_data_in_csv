import csv
from unittest import case

req_file = '/Users/zachnjue/Documents/Scripting/Programming Assignment/ProgrammingAssignment.csv'
string_to_search_for = input(
    "Please search data using either of these string: (1) - Zio code, (2) - State, (3) - City, (4) - Bank, (5) - Type:  ")

file_open = open(req_file, 'r')
data = csv.reader(file_open)


for each_entry in data:
    if string_to_search_for in each_entry:
        print(each_entry)

file_open.close()
