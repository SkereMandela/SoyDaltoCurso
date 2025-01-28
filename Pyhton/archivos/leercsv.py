import csv

with open("archivos\\excel.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)