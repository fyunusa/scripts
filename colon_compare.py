import csv
import os

os.chdir("C:/Users/ZainbaMuhdYunus/Desktop")

with open("Book1.csv") as f:
    cr = csv.reader(f)
    next(cr) # skip title
    col1 = set()
    col2 = set()
    for row in cr:
        col1.add(row[0])
        col2.add(row[1])

with open("output_compare.csv","w",newline="") as f:
    cw = csv.writer(f)
    cw.writerow(["items that are same are"])
    cw.writerows(sorted(col1 & col2))