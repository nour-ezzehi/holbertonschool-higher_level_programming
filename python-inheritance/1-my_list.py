#!/usr/bin/python3
"""new class"""


class MyList(list):
    """my list"""
    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
