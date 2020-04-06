# i want make a py program
# that can read CSV file

import csv

with open('testReadCSV.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
