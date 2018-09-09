#!/usr/bin/env python
import sys
import math
correct = 0
n_lines = 0
n_clss = 0
c_dict = {}
smoothing = 1
w = 999596
for lines in sys.stdin:
    n_lines+=1
    if(n_lines == 1):
        c_dict.update(eval(line))
        for i in c_dict:
            n_clss = n_clss + c_dict[i][0]
        print(c_dict)
    else:
        line = lines.strip()
        test = eval(line)
        for i in test:
            m_probability = -999999999999
            max_class = ""
            for c in c_dict:
                probability = math.log(float(c_dict[c][1])/ (n_clss+1))
                for word in test[i]:
                    j = 1
                if c in eval(test[i][word]):
                    j = j + int(eval(test[i][word])[c])
                    probability = probability + math.log((float(j)+float(smoothing))/(c_dict[c][1]+ w))
                if probability > m_probability:
                    m_probability = probability
                    max_class = c
            if max_class in i[len(i.split(' ')[0])+1:].split(','):
                print "1" + "\t" + "1"
            else:
                print "0" + "\t" + "0"
# print(correct*100)/n_lines
# print(n_lines)