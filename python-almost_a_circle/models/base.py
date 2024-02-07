#!/usr/bin/python3
"""base class"""

import json


class Base:
    """our base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())
        json_dict = cls.to_json_string(list_dicts)

        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation
        json_string"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            inst = cls(4, 2)
        elif cls.__name__ == 'Square':
            inst = cls(4)
        else:
            return None

        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                line = f.read()
                list = cls.from_json_string(line)
                instan_list = []
                for dict in list:
                    instance = cls.create(**dict)
                    instan_list.append(instance)
                return instan_list
        except FileNotFoundError:
            return []
