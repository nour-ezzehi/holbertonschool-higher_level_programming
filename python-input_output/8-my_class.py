#!/usr/bin/python3
"""returns the dictionary description with simple data structure(list,
dictionary, string, integer and boolean) for JSON serialization of an object"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
