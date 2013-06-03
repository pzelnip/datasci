'''
Created on Jun 3, 2013

@author: aparkin
'''
from MapReduce import MapReduce
import sys


mr = MapReduce()


def mapper(record):
    mr.emit_intermediate(record[1][:-10], "does not matter")


def reducer(key, values):
    mr.emit(key)


def main():
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)


if __name__ == "__main__":
    main()