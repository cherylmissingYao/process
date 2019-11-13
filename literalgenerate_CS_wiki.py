from listdir import dump_data, load_data
import os
def relation2literal_generate(path):
    relation2id = load_data(path+"relation2id.pickle")
    #print(relation2id)
    datas = []
    for key in relation2id:
        relation_dict = [relation2id[key], key]
        datas.append(relation_dict)
    #print(datas)
    dump_data(dict(datas), path+"relation2literal.pickle")

def entity2literal_generate(path):
    entity2id = load_data(path+"entity2id.pickle")
    datas = []
    for key in entity2id:
        new_key = entity2id[key]
        if key.find(".txt") != -1:
            f = open(key.replace("\n",""))
            str =f.read()
            str = str.replace("\n", "")
            str = str.replace("\t", "")
            str = str.replace("\r", "")
            literal = str.decode("utf-8", "ignore").encode("unicode-escape")
        else:
            f = open(key+"/definition.txt")
            str = f.read()
            str = str.replace("\n", "")
            str = str.replace("\t", "")
            str = str.replace("\r", "")
            literal = str.decode("utf-8", "ignore").encode("unicode-escape")
        entity_dict= [new_key, literal]
        datas.append(entity_dict)
    #print(datas)
    dump_data(dict(datas),path+"entity2literal.pickle")
#    print(entity2id)
if __name__ == "__main__":
    relation2literal_generate("./data/CS_wiki_sample/")
    entity2literal_generate("./data/CS_wiki_sample/")