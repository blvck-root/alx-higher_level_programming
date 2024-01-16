#!/usr/bin/python3

"""Base module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates the Base class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation"""
        return json.loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs"""
        filename = f"{cls.__name__}.json"

        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        data = cls.to_json_string(list_dicts)
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(json.loads(data), file)

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                json_string = "".join(file.readline())
                data = cls.from_json_string(json_string)
                return [cls.create(**_dict) for _dict in data]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            obj = cls(10, 10)
        elif cls.__name__ == "Square":
            obj = cls(10)
        obj.update(**dictionary)
        return obj
