#!/usr/bin/env python3
from models.base import Base


# create an instance of Base and try out the id and str
base_obj = Base()

print(base_obj)

print(base_obj.to_dict())
