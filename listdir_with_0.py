import os
path = "./data/QAPs"
datas =[]

num =0
def eachFile(filepath):
    global num
    datas = []
    fileNames = os.listdir(filepath)

    for file in fileNames:
        newDir = filepath + '/' + file
        # print(newDir)

        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".txt":
                f = open(newDir)
                str = ""
                for line in f.readlines():
                    str = str + line

                num = num + 1
                #print f.name+":"
                print num
                datas.append(str)
        else:
            eachFile(newDir)

if __name__ == "__main__":
    eachFile(path)

    # print(datas)