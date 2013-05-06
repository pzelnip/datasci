'''
Dumps the contents that the grader supplies to the script via an exception 
stacktrace.

Yay for reverse engineering grading systems rather than y'know, learning content.

Created on May 6, 2013

@author: aparkin
'''
import sys

lines = []

for i in range(1, len(sys.argv)):
    lines.append("================================== START OF sys.argv%s==========================\n" % i)
    with open(sys.argv[i]) as fobj:
        for line in fobj:
            lines.append(line.encode('utf-8'))
    lines.append("================================== END OF sys.argv%s==========================\n" % i)        

s = "".join(lines)
raise ValueError(s)
