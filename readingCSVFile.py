import csv

csvname="/Users/munperum/PycharmProjects/training/data/emp.csv"

with open(csvname) as File:

    reader = csv.reader(File)

    for row in reader:
        print(row)