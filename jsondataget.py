# coding=utf-8
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
path = "/Users/ly/ysy/data/data_structure/getDomainDetailAsRDF.json"
datas =[]
with open(path,"r") as f:
    triple = ""
    temp = json.loads(f.read())
    str = temp['data']
    for key in str:
        triple = triple + key
        str2 = str[key]
        for key2 in str2:
            s = "匿名分面".decode('utf-8')
            if key2.strip().decode('utf-8') == s:
                continue
            #print key2

            str3=str2[key2]
            print str3
            if str3 == "":
                continue

            #print str3[1]
            #time.sleep(3)
            #for key3 in range（len(str3)):
            #    print str3[key3]
            #triple = triple + key2 + str3['assembleText']+line
 #   datas.append(triple)
#print(datas)
