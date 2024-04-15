"""This module models the storage facility used to store objects of the systeem"""
import os
import json

from models.product import Product
from models.product_image import ProductImage


class Storage:
    """Stores objects of the system in a structure called STORE.
    Store has classes that we want to store instances of initialized"""
    # class variables

    # stores instaces of classes of the system
    _STORE = {Product: [],
              ProductImage: []}

    # associates class names to respective classes
    _CLASS_NAMES_AND_CLASSES ={Product.__name__: Product,
                               ProductImage.__name__: ProductImage}
    _DB_FILE = "./db.json"


    def __init__(self):
        # if database file db.json exists 
        # read data into program
        if os.path.exists(Storage._DB_FILE):
            self._read_from_db()

    def add(self, *objects):
        """adds objs to storage"""
        for obj in objects:
            if obj not in self._STORE[obj.__class__]:
                self._STORE[obj.__class__].append(obj)
        #self._persist_to_db()

    def _persist_to_db(self):
        """saves storage objects to file"""
        # convert _STORE to serializable format:
        serializable_format = {}

        for class_, instances in self._STORE.items(): # convert all instances to dict
            serializable_instances = [ instance.to_dict() for instance in instances ]
            serializable_format[class_.__name__] = serializable_instances

        # serialize this new format to json file
        db_file = open(Storage._DB_FILE, 'w', encoding="utf-8")
        json.dump(serializable_format, db_file)
        db_file.close()

    def _read_from_db(self):
        """reads persisted obj data from json file/ db.json into instances"""
        # deserialize the data from file into a dict
        dict_ = None
        try:
            db_file = open(Storage._DB_FILE, "r", encoding="utf-8")
            dict_ = json.load(db_file)
            db_file.close()
        
            # checks to see if dict_ is valid with data befreo perfrom the next
            if type(dict_) is not dict:
                raise Exception("Unable to read data in right format")
        except:
            print("Unable to read from db.json check file for errors")
            return

        # convert the instances from the dict representation to an instance of its class    
        new_dict = {}
        for class_name, instances_dict_reps in dict_.items():
            class_ = self._CLASS_NAMES_AND_CLASSES[class_name]
            instances = [class_(**instance_dict_rep)
                         for instance_dict_rep in instances_dict_reps]
            new_dict[class_] = instances

        # update _STORE with new_dict obects
        self._STORE.update(new_dict)

    def get(self, class_, obj_id):
        """return a single instace of type class_"""
        for obj in self._STORE[class_]:
            if obj.id == obj_id:
                return obj
        return None

    def get_all(self, class_):
        """Returns a tuple of all the instances of a class"""
        return self._STORE[class_]

    def remove(self, obj):
        object_class, object_id = type(obj), obj.id
        self.remove_by_id(object_class, object_id)

    def remove_by_id(self, class_, obj_id):
        """removes an object of a particular class with id obj_id"""
        # find that object and remove it from the list of instances of class_
        obj = None
        index = None
        for index, obj in enumerate(self._STORE[class_]):
            if obj.id == obj_id:
                break
        del self._STORE[class_][index]
        # get related objects from the obj and delete them also
        related_objs = obj.related_objects()
        if related_objs:
            for related_obj in related_objs:
                self.remove(related_obj)
        del obj
        #self._persist_to_db()

    def save(self):
        """saves"""
        self._persist_to_db()

