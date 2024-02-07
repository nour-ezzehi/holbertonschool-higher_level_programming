#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    result = 0
    div = 0
    for tup in my_list:
        div += tup[1]
        result += tup[0] * tup[1]
    return result / div
