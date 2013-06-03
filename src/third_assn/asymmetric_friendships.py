'''
Created on Jun 3, 2013

@author: aparkin
'''

from MapReduce import MapReduce
import sys


mr = MapReduce()


def mapper(record):
    mr.emit_intermediate(tuple(sorted([record[0], record[1]])), record)


def reducer(key, values):
    key2 = (key[1], key[0])
    if len(values) == 1:
        mr.emit(key)
        mr.emit(key2)


def main():
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)


if __name__ == "__main__":
    main()