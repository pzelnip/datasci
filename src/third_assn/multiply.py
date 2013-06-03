'''
Created on Jun 3, 2013

@author: aparkin
'''
from MapReduce import MapReduce
from operator import mul
import sys

MATRIX_A_NUM_ROWS = 5
MATRIX_A_NUM_COLS = 5
MATRIX_B_NUM_ROWS = 5
MATRIX_B_NUM_COLS = 5

mr = MapReduce()


def mapper(record):
    matrix, row, column, value = record
    
    if matrix == "a":
        for k in range(MATRIX_B_NUM_COLS):
            mr.emit_intermediate((row, k), (matrix, column, value))
    elif matrix == "b":
        for i in range(MATRIX_A_NUM_ROWS):
            mr.emit_intermediate((i, column), (matrix, row, value))


def reducer(key, values):
    row, column = key
    
    # reconstruct vectors from A & B
    avect = [0] * MATRIX_A_NUM_COLS
    bvect = [0] * MATRIX_B_NUM_ROWS
    for value in values:
        if value[0] == 'a':
            avect[value[1]] = value[2]
        elif value[0] == 'b':
            bvect[value[1]] = value[2]
    
    # Do scalar product of the two vectors
    result = 0
    for tpl in zip(avect, bvect):
        result += mul(*tpl)
    
    # emit final result
    mr.emit((row, column, result))


def main():
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)


if __name__ == "__main__":
    main()