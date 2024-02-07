#!/usr/bin/python3
"""Rectangle inherits from basegeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate area"""
        return self.__height * self.__width

    def __str__(self):
        """string representation of
        rectangle class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
