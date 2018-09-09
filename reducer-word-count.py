#!/usr/bin/env python
import sys
 
# maps words to their counts
final = dict()

w = set()
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	if('\t'in line):
		# parse the input we got from mapper.py
		word,key = line.split('\t')
		# convert count (currently a string) to int
		key1 = key.split(',')
		if word not in w:
			w.add(word)
			final[word] = dict()
		for k in key1:
			if(k not in final[word]):
				final[word][k] = 1
			else:
				final[word][k] = final[word][k] + 1   
# write the tuples to stdout
# Note: they are unsorted
#print len(w)
for word in final:
	print word+'\t'+str(final[word])
