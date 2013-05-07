import sys
from base64 import *

if len(sys.argv) > 1: # we have an input file!
    inputfile = open(sys.argv[1])
else:
    inputfile = sys.stdin

decode(inputfile, sys.stdout)
