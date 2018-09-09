#!/usr/bin/env python
import sys
import math
import subprocess

cla={}

m = 1
w = 1050054
count = 0
total = 0
total_no_class = 0

for line in sys.stdin:
    total+=1
    if(total == 1):
        cla.update(eval(line))
        for i in cla:
            total_no_class = total_no_class + cla[i][0]
        print(cla)
    else:
        line = line.strip()
        test = eval(line)
        for i in test:
            #print i
            max_prob = -21474836474577454
            max_class = ""
            for c in cla:
                #print('i:{0}, class: {1}'.format(i, c))
                prob = math.log(float(cla[c][1]+ (float(m)/w))/ (total_no_class+1))
                for word in test[i]:
                    j = 1
                    if c in eval(test[i][word]):
                        j = j + int(eval(test[i][word])[c])
                    prob = prob + math.log((float(j)+(float(m)/w))/(cla[c][1]+ m))
                if prob > max_prob:
                    max_prob = prob
                    max_class = c
            if max_class in i[len(i.split(' ')[0])+1:].split(','):
                print "1" + "\t" + "1"
            else:
                print "0" + "\t" + "0"
# print(count*100)/total
# print(total)
