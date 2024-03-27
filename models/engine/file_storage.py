#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    A class FileStorage that serializes instances to a
        JSON file and deserializes JSON file to instances:

        Attributes:
            __file_path (str): The name of the file to save objects to.
            __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        all_objs = FileStorage.__objects

        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised)
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**values)

                        FileStorage.__objects[key] = instance
                except FileNotFoundError:
                    pass
