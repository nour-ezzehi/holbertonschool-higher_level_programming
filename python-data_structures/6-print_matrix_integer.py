#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for tab in matrix:
        for i in range(len(tab) - 1):
            print("{:d}".format(tab[i]), end=" ")
        print("{:d}".format(tab[len(tab) - 1]))
