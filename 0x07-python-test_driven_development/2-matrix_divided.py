#!/usr/bin/python3

"""
The 2-matrix_divided module contains a function that divides a matrix.
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 5)
[[0.2, 0.4, 0.6], [0.8, 1.0, 1.2]]
"""


def matrix_divided(matrix, div):
    """
    Divides each element of a matrix by div.

    Args:
        matrix: a list of lists containing numbers (float or int)
        div: numerical divisor (float or int)

    Returns:
        A new matrix with each element divided by div rounded to 2dp.

    Raises:
        TypeError: If a matrix is not a list of lists, or any element is
        not a number (float or int)
        TypeError: If the rows of a matrix are of different lengths.
        TypeError: If the divisor is non-numerical
        ZeroDivisionError: If the divisor is zero

    Example:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 5)
        [[0.2, 0.4, 0.6], [0.8, 1.0, 1.2]]
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not (
            isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix) and
            all(isinstance(element, (int, float))
                for row in matrix for element in row)
            ):
        raise TypeError(message)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
