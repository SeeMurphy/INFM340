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

