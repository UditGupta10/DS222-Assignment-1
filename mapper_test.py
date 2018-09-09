#!/usr/bin/env python
import sys

count = 0
#--- get all lines from stdin ---
for line in sys.stdin:
	#--- remove leading and trailing whitespace---
	line = line.strip()
	count = count + 1
	#--- split the line into words ---
	words = line.split()
	#--- output tuples [word, 1] in tab-delimited format---
	for word in words[1:]:
		print word+' ~'+'\t'+str(count)+' '+words[0]
