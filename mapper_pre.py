#!/usr/bin/env python
import sys
 
#--- get all lines from stdin ---
for line in sys.stdin:
	#--- remove leading and trailing whitespace---
	line = line.strip()
	print line		
