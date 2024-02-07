#!/usr/bin/python3
"""devide matrix"""


def matrix_divided(matrix, div):
    """devide every matrix item"""

    new_matrix = [[]]
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers / floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers / floats")
        for item in row:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers / floats")
    l = len(matrix[0])
    if not all((len(x) == l)for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row))for row in matrix]
