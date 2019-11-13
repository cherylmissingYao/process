#/home/cheryl/data
import os
path = "/home/cheryl/data/course/"
datas =[]

def readFile(filepath):
    str = ""
    fileNames = filepath+"test.txt"
    f = open(fileNames,"r")

    for line in f.readlines():
        relation = line.split("\t")[1]
        str = str + relation+"\n"
    fileNames = filepath + "train.txt"
    f = open(fileNames, "r")

    for line in f.readlines():
        relation = line.split("\t")[1]
        str = str + relation+"\n"
    fileNames = filepath + "valid.txt"
    f = open(fileNames, "r")

    for line in f.readlines():
        relation = line.split("\t")[1]
        str = str + relation+"\n"

    str2=""
    fileNames = filepath + "new_all.txt"
    f = open(fileNames, "r")

    for line in f.readlines():
        relation = line.split("\t")[1]
        str2 = str2 + relation+"\n"
    s = open(filepath+"old.txt","w")
    s.write(str)

    s = open (filepath +"new.txt","w")
    s.write(str2)
    s.close()
if __name__ == "__main__":
    readFile(path)
 #   print datas