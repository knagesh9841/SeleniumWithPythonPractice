import csv

filename = "CSVFile.csv"

fields = []
rows = []

csvfile = open(filename, "r")

csvreader = csv.reader(csvfile)

rowno = 3

for i in csvreader:
    if csvreader.line_num == 1:
        fields = i.copy()
    elif csvreader.line_num == rowno:
        rows = i.copy()
    else:
        pass

print(fields)
print(rows)

mydict = dict(zip(fields, rows))

print(mydict)