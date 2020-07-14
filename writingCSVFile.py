import csv
emp=[["Muni",100],["Ravi",90],["Raj",80],["Gautam",70]]

csvname="/Users/munperum/PycharmProjects/training/data/emp.csv"

#csv.register_dialect('myDialect',
#quoting=csv.QUOTE_ALL,
#skipinitialspace=True)

with open(csvname,"w") as File: # "a" instead of "w" for append in existing file.

    writerFile = csv.writer(File) #,dialect='myDialect')

    for row in emp:
        writerFile.writerow(row)

File.close()