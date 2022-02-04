import csv

path_to_csv_file = '/Users/zachnjue/Documents/Scripting/Programming Assignment/ProgrammingAssignment.csv'

try:
    string_to_search_for = input(
        "Please search your data using the options listed below : (1) - Zio code, (2) - State, (3) - City, (4) - Bank, (5) - Type:, (6) - Zip code:   ")

    file_open = open(path_to_csv_file, 'r')
    data = csv.reader(file_open)

    for each_entry in data:
        if string_to_search_for in each_entry:
            print(each_entry)
    file_open.close()
except Exception as e:
    print(e)
