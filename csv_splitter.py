import os
import pandas

os.chdir("C:/Users/fyunu/Desktop/csv")

my_csvfile = open('back_update.csv', 'r').readlines()
filename = "new_back_update"
for i in range(len(my_csvfile)):
    if i % 1000 == 0:
        open(str(filename) + '.csv', 'w+').writelines(my_csvfile[i:i+1000])
        filename += 1