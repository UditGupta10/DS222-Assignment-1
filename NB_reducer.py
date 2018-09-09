#!/usr/bin/env python
import sys
correct = 0
total = 0
for lines in sys.stdin:
	line = lines.strip()
	acc = line.split('\t')
	total = total + 1
	if acc[0] == '1':
		correct = correct + 1
print(correct*100)/total
