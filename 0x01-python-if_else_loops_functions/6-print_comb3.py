#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i == 8 and j == 9:
            print("{:02d}".format(i*10 + j))
        elif (i != j):
            print("{:02d},".format(i*10 + j), end=" ")
