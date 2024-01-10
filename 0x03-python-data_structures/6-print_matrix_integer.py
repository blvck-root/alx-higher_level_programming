#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for row in matrix:
        if row:
            for col in row:
                print("{:d}".format(col), end=" " if col != row[-1] else "\n")
