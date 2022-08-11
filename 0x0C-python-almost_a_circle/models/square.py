#!/usr/bin/python3
"""Square model"""
from models.rectangle import Rectangle


class Square(Rectangle):
        """class for square"""
            def __init__(self, size, x=0, y=0, id=None):
                        """initialize the square"""
                                super().__init__(size, size, x, y, id)

                                    @property
                                        def size(self):
                                                    """size getter"""
                                                            return self.width

                                                            @size.setter
                                                                def size(self, value):
                                                                            """size setter"""
                                                                                    self.width = value
                                                                                            self.height = value

                                                                                                def __str__(self):
                                                                                                            """returns information about the shape"""
                                                                                                                    return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                                                                                                                                                                                              self.x,
                                                                                                                                                                                                                              self.y,
                                                                                                                                                                                                                              self.height)

                                                                                                                    def update(self, *args, **kwargs):
                                                                                                                                """updates the square??? i think"""
                                                                                                                                        index = 0
                                                                                                                                                if args is not None and len(args) != 0:
                                                                                                                                                                for argument in args:
                                                                                                                                                                                    index += 1
                                                                                                                                                                                                    if index == 1:
                                                                                                                                                                                                                            self.id = argument
                                                                                                                                                                                                    elif index == 2:
                                                                                                                                                                                                                            self.size = argument
                                                                                                                                                                                                    elif index == 3:
                                                                                                                                                                                                                            self.x = argument
                                                                                                                                                                                                    elif index == 4:
                                                                                                                                                                                                                            self.y = argument
                                                                                                                                                                                                    else:
                                                                                                                                                                                                                    for key, values in kwargs.items():
                                                                                                                                                                                                                                        setattr(self, key, values)

                                                                                                                                                                                                                                            def to_dictionary(self):
                                                                                                                                                                                                                                                        """makes a self dictionary"""
                                                                                                                                                                                                                                                                dictionary = {}
                                                                                                                                                                                                                                                                        for index in ["id", "size", "x", "y"]:
                                                                                                                                                                                                                                                                                        dictionary[index] = getattr(self, index)
                                                                                                                                                                                                                                                                                                return dictionary
