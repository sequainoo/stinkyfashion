#!/usr/bin/env python3
""" The base model of all the objects of the system"""
import uuid


class Base:
    id = ""

    def __init__(self, **kwargs):
        """initializes instances of it"""
        if 'id' not in kwargs:
           self.id = str(uuid.uuid4())
        self.__dict__.update(kwargs)

    def __str__(self):
        """prints [<class name>] (self.id) <self.__dict__>"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        # add object to storage and save storage
        pass

    def to_dict(self):
        dict_ = {}
        dict_.update(self.__dict__)
        #dict_["__class__"] = self.__class__.__name__
        return dict_

    def related_objects(self):
        return None
