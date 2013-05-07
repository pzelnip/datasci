#!/usr/bin/env python

from base64 import *
import sys

if len(sys.argv) > 1: # we have an input file!
    inputfile = open(sys.argv[1])
else:
    inputfile = sys.stdin

with open(sys.argv[1]) as fobj:
    lines = "".join(fobj.readlines())
    s = (standard_b64encode(lines))

template = ''' 
import base64 as foo

string = """%s"""

prog = foo.b64decode(string)
exec prog 
'''
print template % s
