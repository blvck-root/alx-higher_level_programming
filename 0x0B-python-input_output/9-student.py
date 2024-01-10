#!/usr/bin/python3

"""The 9-student module
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object

        Attributes:
          first_name: student name
          last_name: student last name
          age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves dictionary representation of student object
        """
        return self.__dict__
