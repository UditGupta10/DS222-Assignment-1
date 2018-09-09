#!/usr/bin/env python
import sys
 
# maps words to their counts
word2count = dict()
total = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    total = total + 1
    # parse the input we got from mapper.py
    k, count = line.split('\t')
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue
    try:
        word2count[k] = [word2count[k][0]+1,word2count[k][1]+count]
    except:
        word2count[k] = [1,count]
     
# write the tuples to stdout
# Note: they are unsorted
print word2count
