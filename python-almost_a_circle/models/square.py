#!/usr/bin/python3
"""Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ return the representation of a square """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get_method"""
        return self.width

    @size.setter
    def size(self, value):
        """set_method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update"""

        if args and len(args) != 0:
            for idx in range(len(args)):
                if not idx:
                    self.id = args[idx]
                elif idx == 1:
                    self.size = args[idx]
                elif idx == 2:
                    self.x = args[idx]
                elif idx == 3:
                    self.y = args[idx]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary reprentation of a square"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y}
