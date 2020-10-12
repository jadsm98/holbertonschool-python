#!/usr/bin/python3
"""module rectangle"""


import models.base


class Rectangle(models.base.Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if not type(height) is int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if not type(x) is int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if not type(y) is int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not type(height) is int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not type(x) is int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not type(y) is int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__width*self.__height

    def display(self):
        res = '\n'*self.__y
        res += ' '*self.__x + '#'*self.__width
        for i in range(self.__height - 1):
            res += '\n' + ' '*self.__x
            for j in range(self.__width):
                res += '#'
        print(res)
        return res

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):

        if len(args) == 0:
            for k, v in kwargs.items():
                if 'width' in k:
                    self.width = v
                elif 'height' in k:
                    self.height = v
                elif'x' in k:
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
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

    def to_dictionary(self):
        dicts = {'id': self.id, 'width': self._Rectangle__width,
                 'height': self._Rectangle__height, 'x': self._Rectangle__x,
                 'y': self._Rectangle__y}
        return dicts
