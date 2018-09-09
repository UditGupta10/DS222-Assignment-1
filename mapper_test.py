#!/usr/bin/env python
import sys
cnt = 0
for lines in sys.stdin:
	line = lines.strip()
	cnt = cnt + 1
	words = line.split()
	for w in words[1:]:
		print w+' ~'+'\t'+str(cnt)+' '+words[0]
