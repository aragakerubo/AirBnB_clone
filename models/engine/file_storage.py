#!/usr/bin/python3
"""FileStorage module"""
import json
import os


class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        try:
            with open(FileStorage.__file_path, "w") as f:
                json.dump(
                    {
                        key: value.to_dict()
                        for key, value in FileStorage.__objects.items()
                    },
                    f,
                )
        except Exception as e:
            print(e)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = {
                    key: value(**value) for key, value in json.load(f).items()
                }
        except Exception as e:
            print(e)
        if not os.path.exists(FileStorage.__file_path):
            return

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            del FileStorage.__objects[key]
            self.save()

    def close(self):
        """Calls reload method"""
        self.reload()
