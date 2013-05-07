#!/usr/bin/env python

from base64 import b64encode
import sys

if len(sys.argv) > 1: # we have an input file!
    inputfile = open(sys.argv[1])
else:
    inputfile = sys.stdin

with open(sys.argv[1]) as fobj:
    lines = "".join(fobj.readlines())
    s = (b64encode(lines))

print(''' 
import base64 as foo
string = """%s"""
exec (foo.b64decode(string))
''' % s)
