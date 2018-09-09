import string
import math
import time
clss = dict()
dct = dict()
w = set()
alphabets = list(string.ascii_lowercase)
def train():
    f = open("/scratch/ds222-2017/assignment-1/DBPedia.full/full_train.txt",'r')
    ln = f.readline()
    for x in ln:
        words = x.split(" ")
        key = words[0]
        key1 = key.split(',')
        # print(words)
        # print(key)
        # print(key1)
        for k in key1:
            k = k.lower()
            if (k not in clss):
                clss[k] = 1
                dct[k] = dict()
            else:
                clss[k] = clss[k] + 1

        for i in words[1:]:
            i = i.lower()
            w.add(i)
            for k in key1:
                k = k.lower()
                if(i not in dct[k]):
                    dct[k][i] = 1
                else:
                    dct[k][i] = dct[k][i] + 1
    
    print(len(w))
    
    
def test():
    f = open("/scratch/ds222-2017/assignment-1/DBPedia.full/full_test.txt",'r')
    ln = f.readline()
    total_cnt = 0.0
    cnt = 0
    smoothing = 1.0
    lw = len(w)*1.0
    for x in ln:
        total_cnt = total_cnt + 1.0
        words = x.split(" ")
        key = words[0]
        key1 = key.split(',')
        predicted = ""
        max_class = 0.0
        for c in clss:
            clp = (clss[c] + (smoothing / lw)) / sum(clss.values())
            value = math.log10(clp)
            fc = dct[c]
            s = sum(fc.values())*1.0
            for i in words[1:]:
                c = fc.get(i)
                if c is None:
                    v = 1.0;
                else:
                    v = c
                probw = (v + 1.0 + (smoothing / lw)) / (s + smoothing)
                value = value + math.log10(probw)

            if max_class == 0.0:
                max_class = value
            if value > max_class:
                max_class = value
                predicted = c
        
        if predicted in key1:
            cnt = cnt + 1
            
    print((cnt * 100) / total_cnt)  

start = time.time()
train()
test()
print("Total time takem: %f" %(time.time() - start))


