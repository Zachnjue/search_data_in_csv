import csv
def search_cell(string):
    req_file = '/Users/zachnjue/Documents/Scripting/Programming Assignment/ProgrammingAssignment.csv'

    with open(req_file, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            for j, column in enumerate(row):
                if string in column:
                    print((i,j))
                    return (i,j)
    print('nope')
    return 'nope'

data = search_cell("NY")
