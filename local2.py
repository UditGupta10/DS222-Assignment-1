import re
import math
clss = dict()
dct = dict()
w = set()
def train():
    f = open("/scratch/ds222-2017/assignment-1/DBPedia.verysmall/verysmall_train.txt",'r')
    lines = f.readlines()
    for x in lines:
        words = x.split(" ")
        key = words[0]
        key1 = key.split(',')
        for k in key1:
            if (k not in clss):
                clss[k] = 1
                dct[k] = dict()
            else:
                clss[k] = clss[k] + 1

        for i in words[1:]:
            w.add(i)
            for k in key1:
                if(i not in dct[k]):
                    dct[k][i] = 1
                else:
                    dct[k][i] = dct[k][i] + 1
            
    print(len(w))
    
    
def test():
    f = open("/scratch/ds222-2017/assignment-1/DBPedia.verysmall/verysmall_test.txt",'r')
    lines = f.readlines()
    total_cnt = 0
    cnt = 0
    dd=1
    m = 1
    lw = len(w)
    for x in lines:
        total_cnt = total_cnt + 1
        words = x.split(" ")
        key = words[0]
        key1 = key.split(',')
        predicted = ""
        maxi = 0
        for cla in clss:
            clp = (clss[cla]) / sum(clss.values())
            value = math.log10(clp)
            fc = dct[cla]
            s = sum(fc.values())
            for i in words[1:]:
                c = fc.get(i)
                if c is None:
                    v = 1;
                else:
                    v = c
                probw = (v + 1) / (s + lw)
                value = value + math.log10(probw)

            if maxi == 0:
                maxi = value
            if value > maxi:
                maxi = value
                predicted = cla
        
        if predicted in key1:
            cnt = cnt + 1
        
        
    print((cnt * 100) / total_cnt)  


tart = time.time()
train()
test()
print("Total time takem: %f" %(time.time() - start))


