'''
Created on Jun 2, 2013

@author: aparkin
'''
from MapReduce import MapReduce
import sys


mr = MapReduce()

def mapper(record):
    mr.emit_intermediate(record[1], tuple(record))


def reducer(key, values):
    order = None
    for item in values:
        if item[0] == "order":
            order = item
    values.remove(order)
    
    for row in values:
        # use a list because the grader is completely broken
        result = list(order + row)
        mr.emit(result)
    

def main():
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)


if __name__ == "__main__":
    main()