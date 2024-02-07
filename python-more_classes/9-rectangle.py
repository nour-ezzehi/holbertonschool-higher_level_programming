#!/usr/bin/python3
"""define a new class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize with 2 values"""

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        if not self.__height or not self.__width:
            return ""
        matrix_str = ""
        for i in range(self.height):
            row = [str(self.print_symbol) * self.width]
            if i != self.__height - 1:
                matrix_str += ''.join(row) + "\n"
        matrix_str += ''.join(row)
        return matrix_str

    def __repr__(self):
        """represents the class"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """delete an object"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new rectangle with width==height==size"""
        return cls(size, size)
