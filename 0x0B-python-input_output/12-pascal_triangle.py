#!/usr/bin/python3

"""Pascal Trianle Module"""


def pascal_triangle(n):
    """
    Returns lists of lists of integers representing
    the Pascal's triangle of n
    """
    if n <= 0:
        return []

    res = []
    for i in range(n - 1):
        if i == 0:
            res.append([1])
        elif i == 1:
            res.append([1, 2, 1])
        else:
            prev_row = res[i - 1]
            curr_row = [1]
            for j in range(i):
                curr_row.append(prev_row[j] + prev_row[j + 1])
            curr_row.append(1)
            res.append(curr_row)
    return res
