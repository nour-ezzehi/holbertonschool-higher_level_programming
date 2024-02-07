#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """inherits of base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""

        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """width-get_method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width-set_method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height-get_method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height-get_method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x-get_method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x-set_method"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y-get_method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y-set_method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """rectangle's area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """prints the rectangle"""
        for i in range(self.__y):
            print()
        for h in range(self.__height):
            for w in range(self.__width + self.__x):
                if w < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary reprentation of a rectangle"""
        return {
            'id': self.id,
            'x': self.x,
            'width': self.width,
            'height': self.height,
            'y': self.y}
