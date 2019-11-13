import os
import pickle
from sklearn.model_selection import train_test_split
import sys

path = "./data/FaLTs"
datas =[]
num =0
def eachFile(filepath):
    global num
    fileNames = os.listdir(filepath)

    for file in fileNames:
        newDir = filepath + '/' + file
        #print(newDir)
        if os.path.isfile(newDir):
            if file != "definition.txt":

                f = open(newDir)
                str = f.read()
                #for line in f.readlines():
                #    str = str + line
                if str =="":
                    continue
                else:
                    str = str.replace("\n", "")
                    str = str.replace("\t", "")
                    str = str.replace("\r", "")
                    #if file in ["tree"]:
                    #    print("haha")
                    str = str.decode("utf-8", "ignore").encode("unicode-escape")
                #    num = num + 1
                    #print f.name+":"
                    #print num
                #triple = dict(h=filepath, r=file, t=str)
                    #if len(str)<100:
                        #print(str.split())
                    #print(len(str.split()))
                    tail = filepath+"/"+file
                    #datas.append(filepath.replace("\t", "_")+"\t"+file+"\t"+tail+"\n")
                    datas.append(filepath + "\t" + tail + "\t" + tail + "\n")

                #datas.append(triple)
                    #datas.append(len(str.split()))

                    #datas.append("\n")

        else:
            eachFile(newDir)

def dump_data(obj, path):
    with open(path, "w") as writer:
        pickle.dump(obj, writer)
    writer.close()
def write_data(obj, path):
    with open(path, "w") as writer:
        writer.write(obj)
    writer.close()
def load_data(path):
    with open(path) as reader:
        return pickle.load(reader)
def process(path):
    datas = load_data(path)
    #print(type(datas))
    print(datas[0])
    train_valid, test = train_test_split(datas, test_size=0.1)
    train, valid = train_test_split(train_valid, test_size=0.11)

    write_data("".join(train), "./data/CS_wiki_sample/train.txt")
    write_data("".join(valid), "./data/CS_wiki_sample/valid.txt")
    write_data("".join(test), "./data/CS_wiki_sample/test.txt")

if __name__ == "__main__":
    eachFile(path)
    #print datas
    #print len(datas)
    #write_data("".join(datas), "./data/CS_wiki.triple")
    dump_data(datas, "./data/kf_sample.triple")
    #print("".join(map(str, datas)))
    #write_data("".join(map(str, datas)), "./data/len.txt")
    #with open("./data/kf1.triple", "w") as f:
    #    pickle.dump(datas, f)
    process("./data/kf_sample.triple")