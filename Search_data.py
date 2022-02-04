import csv

req_file = '/Users/zachnjue/Documents/Scripting/Programming Assignment/ProgrammingAssignment.csv'
stringr
string = 'Dallas'

file_open = open(req_file, 'r')
data = csv.reader(file_open)


for each_entry in data:
    if string in each_entry:
        print(each_entry)
file_open.close()
