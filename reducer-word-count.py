#!/usr/bin/env python
import sys
dct = dict()
wrd = set()
for line in sys.stdin:
	line = line.strip()
	if('\t'in line):
		w,key = line.split('\t')
		key1 = key.split(',')
		if w not in wrd:
			wrd.add(w)
			dct[w] = dict()
		for k in key1:
			if(k not in dct[w]):
				dct[w][k] = 1
			else:
				dct[w][k] = dct[w][k] + 1   
for w in dct:
	print w+'\t'+str(dct[w])
