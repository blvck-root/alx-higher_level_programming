#!/usr/bin/python3

"""Square module"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates the Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides __str__ function"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of a square"""
        self.width = value
        self.height = value

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
            self.size = args[1]
        if n_args >= 3:
            self.x = args[2]
        if n_args >= 4:
            self.y = args[3]

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.width}
