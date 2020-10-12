#!/usr/bin/python3
"""module Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """inherits from rectangle"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """formatting the string"""

        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""

        return self.width

    @size.setter
    def size(self, v):
        """size setter"""

        if not type(v) is int:
            raise TypeError("width must be an integer")
        elif v <= 0:
            raise ValueError("width must be > 0")
        self.width = v
        self.height = v

    def update(self, *args, **kwargs):
        """update instance"""

        if len(args) == 0:
            for k, v in kwargs.items():
                if 'size' in k:
                    self.size = v
                elif 'x' in k:
                    self.x = v
                elif 'y' in k:
                    self.y = v
                elif 'id' in k:
                    self.id = v
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

    def to_dictionary(self):
        """ to dictionary"""

        dicts = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dicts
