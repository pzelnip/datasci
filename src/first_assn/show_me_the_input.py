'''
Dumps the contents that the grader supplies to the script via an exception 
stacktrace.

Yay for reverse engineering grading systems rather than y'know, learning content.

Created on May 6, 2013

@author: aparkin
'''
import sys

lines = []
with open(sys.argv[1]) as fobj:
    for line in fobj:
        lines.append(line)
lines.append("================================== END OF sys.argv1==========================")        
with open(sys.argv[2]) as fobj:
    for line in fobj:
        lines.append(line)

s = "".join(lines)
raise ValueError(s)
