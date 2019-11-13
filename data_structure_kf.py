import os
path = "/Users/ly/ysy/data/data_structure"
datas =[]

def eachFile(filepath):
    fileNames = os.listdir(filepath)

    for file in fileNames:
        newDir = filepath + '/' + file
        # print(newDir)

        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".json":
                f = open(newDir,"r")
                f=f.read()
                f=f.replace(':{"',':\r\n{"')
                s = open(newDir+"_new","w")
                s.write(f)
                s.close()
        else:
            eachFile(newDir)

if __name__ == "__main__":
    eachFile(path)

    # print(datas)