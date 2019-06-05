import os, os.path
import xml.etree.ElementTree as ET
import xlsxwriter
import re
import fileinput


path_ = "\\drive.irds.uwa.edu.au\\PMC-LD-001\\dataset\\"
        # "0001_American_Beauty\\"

list_of_dirs = []



row = 2

file_to_read = "C:\\Users\\22649731\\Desktop\\Yulia\\UWA\\Video_Captioning\\code\\dataset\\LSMDC - short\\MPIIMD_downloadLinks.txt"

# with open(file_to_read, "r") as f:
#     lines = f.readlines()
#
#
# data = open(file_to_read).read()
path, dirs, files = next(os.walk(path_))
file_count = len(files)

for dir in os.listdir(path_):
    for entry in os.listdir(os.path.join(path_, dir)):
        if os.path.isfile(os.path.join(path_,dir, entry)):
            phrase = entry
            print(entry)
            for line in fileinput.input(file_to_read, inplace=True):
                if phrase in line:
                    continue
                print(line, end='')
