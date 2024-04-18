#!/usr/bin/env python
"""Model of product being sold hwihc is a cloth"""
from .base import Base


class Product(Base):
    title = ""
    description = ""
    price = 0.0
    sex = ""
    feature = False
    #images_ids = [] # a list of ids of image objects

    def __init__(self, **kwargs):
        #self._images = kwargs['images_ids']
        #del kwargs['images_ids']
        super().__init__(**kwargs)

    def images(self):
        """returns a list of ProductImage objects related to this object"""
        from storage.engine import storage_engine
        from .product_image import ProductImage
        return [image 
                for image in storage_engine.get_all(ProductImage)
                if image.product_id == self.id]

    #def __delete__(self):
    #    """it finds associated objects (by_id) and execute delete on them"""
    #    pass

    def related_objects(self):
        return self.images()

    def is_male(self):
        return self.sex.upper() == 'M' or self.sex.upper() == "MALE"
    
    def is_female(self):
        return self.sex.upper() == 'F' or self.sex.upper() == "FEMALE"
    
    def is_unisex(self):
        """tells if its unisex"""
        return self.sex.upper() == 'U' or self.sex.upper() == "UNISEX"
    
    def should_be_featured(self):
        """tells if a product should be featured"""
        return self.feature
        
