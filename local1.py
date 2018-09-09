import re
import string
import math
import time
classes = dict()
final = dict()
w = set()
alphabets = list(string.ascii_lowercase)
def train():
    f = open("/scratch/ds222-2017/assignment-1/DBPedia.full/full_train.txt",'r')
    lines = f.readlines()
    for x in lines:
        words = x.split(" ")
        key = words[0]
        key1 = key.split(',')
        # print(words)
        # print(key)
        # print(key1)
        for k in key1:
            k = k.lower()
            if (k not in classes):
                classes[k] = 1
                final[k] = dict()
            else:
                classes[k] = classes[k] + 1

        for i in words[1:]:
            #i = re.sub(r'[^\w\s]','',i)
            # if(i[0] not in alphabets):
            #     continue
            i = i.lower()
            w.add(i)
            for k in key1:
                k = k.lower()
                if(i not in final[k]):
                    final[k][i] = 1
                else:
                    final[k][i] = final[k][i] + 1
    
    print(len(w))
    
    
def test():
    f = open("/scratch/ds222-2017/assignment-1/DBPedia.full/full_test.txt",'r')
    lines = f.readlines()
    total_count = 0.0
    count = 0
    dd=1.0
    m = 1.0
    lw = len(w)*1.0
    for x in lines:
        total_count = total_count + 1.0
        words = x.split(" ")
        key = words[0]
        key1 = key.split(',')
        predicted = ""
        maxi = 0.0
        for cla in classes:
            
            clp = (classes[cla] + (m / lw)) / sum(classes.values())
            value = math.log10(clp)
            fc = final[cla]
            s = sum(fc.values())*1.0
            for i in words[1:]:
                i = re.sub(r'[^\w\s]','',i)
                c = fc.get(i)
                if c is None:
                    v = 1.0;
                else:
                    v = c
                probw = (v + 1.0 + (m / lw)) / (s + m)
                value = value + math.log10(probw)

            if maxi == 0.0:
                maxi = value
            if value > maxi:
                maxi = value
                predicted = cla
        
        if predicted in key1:
            count = count + 1

        if total_count%5000 == 0:
            print("No. of lines %i, correctly classified: %i" %(total_count, count))
        
        
    print((count * 100) / total_count)  

start = time.time()
train()
test()
print("Total time takem: %f" %(time.time() - start))
#print(sum(classes.values()))
#print(final['English-language_journals'])

