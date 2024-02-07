#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = list(set(my_list))
    total = 0
    for item in new:
        total += item
    return total
