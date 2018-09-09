import re
import math
classes = dict()
final = dict()
w = set()
def train():
    f = open("/scratch/ds222-2017/assignment-1/DBPedia.verysmall/verysmall_train.txt",'r')
    lines = f.readlines()
    for x in lines:
        words = x.split(" ")
        key = words[0]
        key1 = key.split(',')
        for k in key1:
            if (k not in classes):
                classes[k] = 1
                final[k] = dict()
            else:
                classes[k] = classes[k] + 1

        for i in words[1:]:
            i = re.sub(r'[^\w\s]','',i)
            w.add(i)
            for k in key1:
                if(i not in final[k]):
                    final[k][i] = 1
                else:
                    final[k][i] = final[k][i] + 1
            
    print(len(w))
    
    
def test():
    f = open("/scratch/ds222-2017/assignment-1/DBPedia.verysmall/verysmall_test.txt",'r')
    lines = f.readlines()
    total_count = 0
    count = 0
    dd=1
    m = 1
    lw = len(w)
    for x in lines:
        total_count = total_count + 1
        words = x.split(" ")
        key = words[0]
        key1 = key.split(',')
        predicted = ""
        maxi = 0
        for cla in classes:
            
            clp = (classes[cla]) / sum(classes.values())
            value = math.log10(clp)
            fc = final[cla]
            s = sum(fc.values())
            for i in words[1:]:
                i = re.sub(r'[^\w\s]','',i)
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
            count = count + 1

        if total_count%10000 == 0:
                print(total_count)
        
        
    print((count * 100) / total_count)  


train()
test()
#print(sum(classes.values()))
#print(final['English-language_journals'])

