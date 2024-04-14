#!/usr/bin/env python
"""Model of product being sold hwihc is a cloth"""
from base import Base


class Product(Base):
    name = ""
    description = ""
    price = 0.0
    #images_ids = [] # a list of ids of image objects

    def __init__(self, **kwargs):
        #self._images = kwargs['images_ids']
        #del kwargs['images_ids']
        super().__init__(**kwargs)

    def images(self):
        """returns a list of ProductImage objects related to this object"""
        pass

