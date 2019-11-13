import os
import time
path = "/Users/ly/ysy/data/triple.json"
datas =[]
f = open(path,"r")
f=f.read()
f.replace("], [","],\r\n[")
b = eval(f)
size = len(b)
strs = []
num = 0
#s = open("./data/triple.json","w")
#s.write(f)
#s.close()
for i in range(1,size):
    #if str(b[i][2]) == "v t e Tree data structures Search trees (dynamic sets/associative arrays) 2\\u20133 2\\u20133\\u20134 AA (a,b) AVL B B+ B* Bx (Optimal)\\u00a0Binary search Dancing HTree Interval Order statistic (Left-leaning)\\u00a0Red-black Scapegoat Splay T Treap UB Weight-balanced Heaps Binary Binomial Brodal Fibonacci Leftist Pairing Skew Van Emde Boas Weak Tries Ctrie C-trie (compressed ADT) Hash Radix Suffix Ternary search X-fast Y-fast Spatial data partitioning trees Ball BK BSP Cartesian Hilbert R k-d (implicit k-d) M Metric MVP Octree Priority R Quad R R+ R* Segment VP X Other trees Cover Exponential Fenwick Finger Fractal tree index Fusion Hash calendar iDistance K-ary Left-child right-sibling Link/cut Log-structured merge Merkle PQ Range SPQR Top":

    if str(b[i][2]).find("The performance") != -1:
        print b[i][2]
            #print b[i]
        num = num+1
print num



