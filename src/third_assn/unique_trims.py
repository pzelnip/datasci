'''
Created on Jun 3, 2013

@author: aparkin
'''
from MapReduce import MapReduce
import sys


mr = MapReduce()


def mapper(record):
    nucleotide = record[1]
    nucleotide = nucleotide[:-10]
    mr.emit_intermediate(nucleotide, "does not matter")


def reducer(key, values):
    mr.emit(key)


def main():
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)


if __name__ == "__main__":
    main()