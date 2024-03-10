#!/usr/bin/python3
"""BaseModel module"""
import datetime
import uuid
import json
from os import path
from models import storage


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
