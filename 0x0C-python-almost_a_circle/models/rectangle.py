#!/usr/bin/python3

"""Rectangle module"""
from .base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of a rectangle object"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of a rectangle object"""
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """Get the height of a rectangle object"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a rectangle object"""
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the y-coordinate of a rectangle object"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of a rectangle object"""
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of a rectangle object"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of a rectangle object"""
        self.validate("y", value)
        self.__y = value

    @staticmethod
    def validate(name, value):
        """Validate input"""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")

        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(f"{name} must be > 0")

        if (name == "x" or name == "y") and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Display a rectangle using the # character"""
        for _ in range(self.y):
            print("")

        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update attributes- order of args is important
        Order: id, width, height, x, y
        """
        n_args = len(args)
        if n_args == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

        if n_args >= 1:
            self.id = args[0]
        if n_args >= 2:
            self.width = args[1]
        if n_args >= 3:
            self.height = args[2]
        if n_args >= 4:
            self.x = args[3]
        if n_args >= 5:
            self.y = args[4]

    def to_dictionary(self):
        """Returns dictionary representation of a rectangle"""
        _dict = {'x': self.x, 'y': self.y, 'id': self.id,
                 'height': self.height, 'width': self.width}
        return _dict

    def __str__(self):
        """Override the __str__ method"""
        string = f"[Rectangle] ({self.id}) {self.x}/{self.y} "
        string += f"- {self.width}/{self.height}"
        return string
