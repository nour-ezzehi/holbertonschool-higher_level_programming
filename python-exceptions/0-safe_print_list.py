#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in range(0, x):
            if isinstance(my_list[i], int):
                print("{}".format(my_list[i]), end='')
                i += 1
    except IndexError:
        None
    print()
    return i
