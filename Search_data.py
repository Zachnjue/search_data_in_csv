import csv

path_to_csv_file = '/Users/zachnjue/Documents/Scripting/Programming Assignment/ProgrammingAssignment.csv'

try:
    string_to_search_for = input(
        "Please search your data using the options listed below:\n(1) - Zip code,\n(2) - State,\n(3) - City,\n(4) - Bank,\n(5) - Type:,\n(6) - Zip code:\n   ")

    file_open = open(path_to_csv_file, 'r')
    data = csv.reader(file_open)

    for each_entry in data:
        if string_to_search_for in each_entry:
            print(each_entry)
    file_open.close()
except Exception as e:
    print(e)
