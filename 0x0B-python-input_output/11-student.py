#!/usr/bin/python3

"""
The 11-student module
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

    def to_json(self, attrs=None):
        """
        Retrieves dictionary representation of student object
        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for k, v in json.items():
            self.__setattr__(k, v)
