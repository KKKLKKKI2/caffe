# encoding utf-8
import os
#import xlrd
import openfile

def readtxt(dataname):
    file = openfile.read_file(dataname)
    data_list = []

    done = 0
    while not done:
        aLine = file.readline()
        aLine = aLine.replace('\t','')
        if (aLine != ''):
            data_list.append(aLine)
        else:
            done = 1

    file.close()
    return data_list

def dirs_readtxt(dir, filename):
    file = openfile.dirs_read_file(dir, filename)
    data_list = []

    done = 0
    while not done:
        aLine = file.readline()
        aLine = aLine.replace('\t','')
        if (aLine != ''):
            data_list.append(aLine)
        else:
            done = 1

    file.close()
    return data_list

'''
file = "Moth_Family"
list = readtxt(file)
print(len(list))
print(list)
counter = 0
for item in list:
    counter += 1
    print(list[counter])
    if (counter == 102):
        break
'''



