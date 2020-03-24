import os
import glob
import pandas as pd

os.chdir("C:/Users/ZainbaMuhdYunus/Desktop")
a = pd.read_csv("try.csv")
b = pd.read_csv("try_rp.csv")
# skip out axis 
# b = b.dropna(axis=1)
merged = pd.concat(b, on='uniqueID,Title,Resource Person,Topics,Keywords,Language,Reciter,Audio URL,AMR Audio File,Verse Ref,AlbumID,Duration,Duration Range,MP3 Size Range')
# merged = a.merge(b)
# merged = pd.concat([a, b])
merged.to_csv("output1.csv", index=False)


import csv

with open("test.csv") as f:
    cr = csv.reader(f)
    next(cr) # skip title
    col1 = set()
    col2 = set()
    for a,b in cr:
        col1.add(a)
        col2.add(b)

with open("output.csv","w",newline="") as f:
    cw = csv.writer(f)
    cw.writerow(["item"])
    cw.writerows(sorted(col1 & col2))
