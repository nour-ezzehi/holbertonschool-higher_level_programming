#!/usr/bin/python3
"""define a new class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize with 2 values"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width_getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """width_setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height_getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """height_setter"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle's area"""

        return self.__height * self.__width

    def perimeter(self):
        """returns rectangle's perimeter"""
        if not self.__width or not self.__height:
            return 0
        return (self.__height + self.__width) * 2
