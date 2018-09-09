#!/usr/bin/env python
import sys

#--- get all lines from stdin ---
for line in sys.stdin:
	#--- remove leading and trailing whitespace---
	#line = line.strip()

	#--- split the line into words ---
	words = line.split()
	if(line):
		key = words[0].split(',')
		for k in key:
			print k +'\t'+str(len(words[1:]))
