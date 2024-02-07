#!/usr/bin/python3
"""prints the square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """initialise with a given size"""
        self.__size = size

    @property
    def size(self):
        """getter"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate area of a square"""

        return self.__size ** 2

    def my_print(self):
        """prints the square"""

        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print('#', end='')
                print()
