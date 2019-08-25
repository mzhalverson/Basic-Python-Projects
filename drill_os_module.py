#
# Python:   3.7.3
#
# Author:   Mollie Zechlin
#
# Purpose:  The Tech Academy - Python Course, Creating my first drill.
#



import os


path = "C:\\Users\\Kevin\\molz\\Drill_OS\\"

file_list = os.listdir(path)

for file in file_list:
    name, ext = os.path.splitext(file)
    
    if ext == '.txt':
        abspath = os.path.join(path, file)
        last_rev = os.path.getmtime(abspath)
        print(abspath, '\n', last_rev)        


