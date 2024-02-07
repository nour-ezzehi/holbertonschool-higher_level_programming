#!/usr/bin/python3
"""instantiation with an iteger value"""


class Square:
    """square class"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate area of a square"""

        return self.__size ** 2
