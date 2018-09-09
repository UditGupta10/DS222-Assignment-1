#!/usr/bin/env python
import sys
 
# maps words to their counts
count = 0
total = 0
for line in sys.stdin:
	line = line.strip()
	acc = line.split('\t')
	total = total + 1
	if acc[0] == '1':
		count = count + 1
print(count*100)/total
