#!/usr/bin/env python
import sys
for lines in sys.stdin:
    line = lines.strip()
    word = line.split()
    if(line):
        clss = word[0]
    for w in word[1:]:
        print w+'\t'+ clss
	
