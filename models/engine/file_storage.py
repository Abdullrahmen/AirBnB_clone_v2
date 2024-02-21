#!/usr/bin/python3
"""FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex


class FileStorage:
    """FileStorage class that serializes instances to a JSON file
       and deserializes JSON file to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """Return all the objects"""
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects
        
    
    def new(self, obj):
        """Add a new object"""
        if obj:
            key = "{}.{}".format(type(obj.__name__), obj.id)
            self.__objects[key] = obj
        
    def save(self):
        """Save all objects to a json file"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)
            
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
        
    def delete(self, obj=None):
        """ delete an existing element"""
        if obj:
            key = "{}.{}".format(type(obj.__name__), obj.id)
            del self.__objects[key]