#!/usr/bin/python3
"""class_comparaison"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance
    of the specified class ; otherwise False"""
    return type(obj) is a_class
