#!/usr/bin/env python
import sys
 
# maps words to their counts
word2count = {}
value = "" 
key = ""
final = dict()
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	if(line):
		words = line.split('\t')
		if words[0] != '~':
			if words[0][-1] == '~':
				idn = words[1]
				if idn not in final:
					final[idn] = dict()
				if words[0][:-2] == key:
					final[idn][words[0][:-2]] = value
			else:
				key = words[0]
				value = words[1]

#print final
for i in final:
	d=dict()
	d[i] = final[i]
	print str(d)
