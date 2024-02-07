#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l1 = sorted(a_dictionary.keys())
    for key in l1:
        print("{}: {}".format(key, a_dictionary[key]))
