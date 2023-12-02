#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for row in matrix:
        for i in range(len(row) - 1):
            print("{:d}".format(row[i]), end=" ")
	print("{:d}".format(row[-1]))
