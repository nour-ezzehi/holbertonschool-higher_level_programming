#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = my_list[0]
    for _ in range(1, len(my_list)):
        if my_list[_] > max:
            max = my_list[_]
    return max
