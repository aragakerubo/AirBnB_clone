#!/usr/bin/python3
"""BaseModel module"""
import datetime
import uuid
import json
from os import path
from models import storage


# 5. Store first object
# mandatory
# Now we can recreate a BaseModel from another one by using a dictionary representation:

# <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
# It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.

# Writing the dictionary representation to a file won’t be relevant:

# Python doesn’t know how to convert a string to a dictionary (easily)
# It’s not human readable
# Using this file with another program in Python or other language will be hard.
# So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

# Now the flow of serialization-deserialization will be:

# <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
# Magic right?

# Terms:

# simple Python data structure: Dictionaries, arrays, number and string. ex: { '12': { 'numbers': [1, 2, 3], 'name': "John" } }
# JSON string representation: String representing a simple data structure in JSON format. ex: '{ "12": { "numbers": [1, 2, 3], "name": "John" } }'


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """BaseModel constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(
                        self,
                        key,
                        datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                        ),
                    )
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """__str__ method"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """save method"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """to_dict method"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy

    def store(self):
        """store method"""

        if not path.exists("file.json"):
            with open("file.json", "w") as f:
                f.write("{}")
        with open("file.json", "r") as f:
            all_objs = json.load(f)
        all_objs[self.id] = self.to_dict()
        with open("file.json", "w") as f:
            json.dump(all_objs, f)
        storage.reload()
        return self

    def reload(self):
        """reload method"""

        if path.exists("file.json"):
            with open("file.json", "r") as f:
                all_objs = json.load(f)
            for key, value in all_objs.items():
                storage.all()[key] = eval(value["__class__"])(**value)


# 4. Create BaseModel from dictionary
# Previously we created a method to generate a dictionary representation of an instance (method to_dict()).
# Now it’s time to re-create an instance with this dictionary representation.
# <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>


# class BaseModel:
#     """BaseModel class"""

#     def __init__(self, *args, **kwargs):
#         """BaseModel constructor"""
#         if kwargs:
#             for key, value in kwargs.items():
#                 if key == "created_at" or key == "updated_at":
#                     setattr(
#                         self,
#                         key,
#                         datetime.datetime.strptime(
#                             value, "%Y-%m-%dT%H:%M:%S.%f"
#                         ),
#                     )
#                 elif key != "__class__":
#                     setattr(self, key, value)
#         else:
#             self.id = str(uuid.uuid4())
#             self.created_at = datetime.datetime.now()
#             self.updated_at = datetime.datetime.now()

#     def __str__(self):
#         """__str__ method"""
#         return "[{}] ({}) {}".format(
#             self.__class__.__name__, self.id, self.__dict__
#         )

#     def save(self):
#         """save method"""
#         self.updated_at = datetime.datetime.now()

#     def to_dict(self):
#         """to_dict method"""
#         dict_copy = self.__dict__.copy()
#         dict_copy["__class__"] = self.__class__.__name__
#         dict_copy["created_at"] = self.created_at.isoformat()
#         dict_copy["updated_at"] = self.updated_at.isoformat()
#         return dict_copy


# 3. BaseModel
# Write a class BaseModel that defines all common attributes/methods for other classes:
# class BaseModel:
#     """BaseModel class"""

#     def __init__(self):
#         """BaseModel constructor"""
#         self.id = str(uuid.uuid4())
#         self.created_at = datetime.datetime.now()
#         self.updated_at = datetime.datetime.now()

#     def __str__(self):
#         """__str__ method"""
#         return "[{}] ({}) {}".format(
#             self.__class__.__name__, self.id, self.__dict__
#         )

#     def save(self):
#         """save method"""
#         self.updated_at = datetime.datetime.now()

#     def to_dict(self):
#         """to_dict method"""
#         dict_copy = self.__dict__.copy()
#         dict_copy["__class__"] = self.__class__.__name__
#         dict_copy["created_at"] = self.created_at.isoformat()
#         dict_copy["updated_at"] = self.updated_at.isoformat()
#         return dict_copy
