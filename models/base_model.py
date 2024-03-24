#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
        """
        A base class for models with common attributes.

        Attributes:
            id (uuid.UUID): A unique identifier generated using UUID4.
            created_at (datetime.datetime): The timestamp when the model instance was created.
            updated_at (datetime.datetime): The timestamp when the model instance was last updated.

        Methods:
        __init__: Initializes a BaseModel instance.
        """

        def __init__(self):
            """
            Initializes a BaseModel instance
            """

            self.id = str(uuid.uuid4())

            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        def __str__(self):
            """
            Returns string representation of BaseModel
            """
    
            class_name = self.__class__.__name__
            return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

        def save(self):
            """
            Updates the public instance attribute updated_at with the current datetime.

            """

            self.updated_at = datetime.now()

        def to_dict(self):
            """
            Returns a dictionary containing all keys/values of __dict__ of the instance.

            """

            inst_dict = self.__dict__.copy()
            inst_dict["__class__"] = self.__class__.__name__
            inst_dict["created_at"] = self.created_at.isoformat()
            inst_dict["updated_at"] = self.updated_at.isoformat()
    
            return inst_dict

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

