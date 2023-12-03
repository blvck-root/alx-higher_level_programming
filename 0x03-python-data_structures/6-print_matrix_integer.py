#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix[0]:
        for row in matrix:
            if row:
                for i in range(len(row) - 1):
                    print("{:d}".format(row[i]), end=" ")
                print("{:d}".format(row[-1]))
