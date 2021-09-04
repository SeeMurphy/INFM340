# This is a python script to display the first 10 rows of a csv file on Netflix stock value.
# Importing CSV Library
import csv
# file name
filename = "netflix.csv"
# Fields and Rows list
fields = []
rows = []
# reading csv
with open(filename, 'r') as csvfile:
    # csv reader object
    csvreader = csv.reader(csvfile)
    # extracting field names
    fields = next(csvreader)
    # extracting data rows
    for row in csvreader:
        rows.append(row)
    # total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
# printing the field names
print('Field names are: ' + ', '.join(field for field in fields))
# printing the first 10 rows
print('\nFirst 10 rows are:\n')
for row in rows[:10]:
    #parsing
    for col in row:
        print("%10s"%col),
    print('\n')

