import xlsxwriter
import csv
import os 

os.chdir("C:/Users/ZainbaMuhdYunus/Desktop/py_images")

# Creating a new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('images4.xlsx')
worksheet = workbook.add_worksheet()

# Widenening the first column
worksheet.set_column('A:A', 30)

# Inserting my image.
worksheet.write('A2', 'I am the first image:')
worksheet.insert_image('B2' , 'ges-4.jpg',{'x_scale': 0.3, 'y_scale': 0.3})

workbook.close()