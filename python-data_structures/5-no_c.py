#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for _ in range(len(my_string)):
        if my_string[_].upper() == 'C':
            continue
        new_string += my_string[_]
    return new_string
