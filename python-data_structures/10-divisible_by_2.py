#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new = []
    for _ in range(len(my_list)):
        if not (my_list[_] % 2):
            new.append(True)
        else:
            new.append(False)
    return new
