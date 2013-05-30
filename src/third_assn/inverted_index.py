'''
Created on May 30, 2013

@author: aparkin
'''
from MapReduce import MapReduce
import sys
 
mr = MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, 1)

def reducer(key, values):
    total = 0
    for v in values:
        total += v
    mr.emit((key, total))


def main():
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)

if __name__ == "__main__":
    main()