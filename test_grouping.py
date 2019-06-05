import os, os.path
import xml.etree.ElementTree as ET
import xlsxwriter
import re

path_ = "E:\\dataset\\"
workbook = xlsxwriter.Workbook('C:/Users/22649731/Desktop/movies.xlsx')
worksheet = workbook.add_worksheet()

row = 2

file_to_read = "C:\\Users\\22649731\\Desktop\\Yulia\\UWA\\Video_Captioning\\code\\dataset\\LSMDC - short\\MPIIMD_downloadLinks.txt"
data = open(file_to_read).read()
path, dirs, files = next(os.walk(path_))
file_count = len(files)

for i in dirs:
    path2, dirs2, files2 = next(os.walk(os.path.join(path_ + i)))
    worksheet.write(row, 1, i)
    worksheet.write(row, 2, len(files2))
    count = data.count(i)
    worksheet.write(row, 3, count / 2)
    row = row + 1


workbook.close()
print(row)