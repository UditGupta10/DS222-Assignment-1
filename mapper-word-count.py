#!/usr/bin/env python
import sys
import re
l=list()
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
#--- get all lines from stdin ---
for line in sys.stdin:
    #--- remove leading and trailing whitespace---
    line = line.strip()

    #--- split the line into words ---
    words = line.split()
    if(line):
        key = words[0]

    #--- output tuples [word, 1] in tab-delimited format---
    for s in words[1:]:
        print re.sub(r'[^\w\s]','',s)+'\t'+ key
	
