#!/usr/bin/env python
import sys
wtc = dict()
total = 0
for lines in sys.stdin:
    line = lines.strip()
    total = total + 1
    k, c = line.split('\t')
    c = int(c)
    try:
        wtc[k] = [wtc[k][0]+1,wtc[k][1]+c]
    except:
        wtc[k] = [1,c]
print wtc
