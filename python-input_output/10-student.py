#!/usr/bin/python3
"""student class"""


class Student:
    """the student class"""
    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        s = {}
        for item in attrs:
            if hasattr(self, item):
                s[item] = getattr(self, item)
        return s
