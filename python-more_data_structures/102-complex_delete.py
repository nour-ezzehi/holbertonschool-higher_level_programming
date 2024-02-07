#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tab = a_dictionary.copy()
    for key, val in tab.items():
        if val == value:
            a_dictionary.pop(key)
    return a_dictionary
