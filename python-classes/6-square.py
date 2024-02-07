#!/usr/bin/python3
"""prints the square"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialise with a given size"""
        self.__size = size
        self.__position = position

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
        else:
            self.__size = value

    @property
    def position(self):
        """position getter"""

        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if len(value) != 2 or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate area of a square"""

        return self.__size ** 2

    def my_print(self):
        """prints the square"""

        if self.__size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
